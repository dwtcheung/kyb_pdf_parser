'''
This is a demo of using ollama ocr to read a company profile and extracting it to JSON
Specifically for PDF with pages consisting of images instead of actual text
Note that it the LLM is not perfect when it come to OCR
'''

import pymupdf, json
from ollama_ocr import OCRProcessor
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings
from models.SG_ACRA import SGCompany
from timeit import default_timer as timer



# File path of the PDF, change it for where you store PDF
doc = pymupdf.open("D:\\python_projects\\pdf_llama_index\\sg_sample.pdf")

'''
Need 3 different LLM for OCR
* Vision, not all vision models work, library author mentioned LLaVA can generate wrong output
* Embedding
* Markdown processing to JSON model
'''
ocr = OCRProcessor(model_name='llama3.2-vision')
llm = Ollama(model="zephyr",
             base_url="http://127.0.0.1:11434",
             request_timeout=180,
             keep_alive=1,
             num_gpu=1,
             temperature=0)

Settings.llm = llm
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

pagecount = 0
resultText = ""

start = timer()
'''
Read one page at a time and save it as an image
Read the saved image using Ollama OCR and save as Markdown
'''
for page in doc:
    text = ""
    pixmap = page.get_pixmap(dpi=300)
    filename = "D:\\python_projects\\pdf_llama_index\\sg_images\\temp" + str(pagecount) + ".jpg"
    pixmap.pil_save(filename, dpi=(300,300))
    pagecount += 1
    text += ocr.process_image(
        image_path=filename,
        format_type="markdown"
    )
    resultText += text

# Defined the JSON model to use for structured output
sllm = llm.as_structured_llm(output_cls=SGCompany)

response = sllm.complete(resultText)
json_response = json.loads(response.text)
end = timer()
print(resultText)
print("\n")
print(json.dumps(json_response,indent=2))
print("\nTime required:")
print(end-start)
