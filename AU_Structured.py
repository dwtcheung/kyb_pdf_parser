'''
This is a demo of using ollama to read a company profile and extracting it to JSON
Specifically for PDF that actually contain text and structure and not just an image
'''

import json

from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings
from models.AU_ASIC import AUCompany
from pymupdf4llm import LlamaMarkdownReader
from timeit import default_timer as timer

'''
Need 2 different LLM to process PDF to JSON
* Embed
* Parse Markdown to JSON
'''
llm = Ollama(model="zephyr",
             base_url="http://127.0.0.1:11434",
             request_timeout=180,
             keep_alive=1,
             num_gpu=1,
             temperature=0)

Settings.llm = llm
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

start = timer()
md_read = LlamaMarkdownReader()
data = md_read.load_data("D:\\python_projects\\pdf_llama_index\\au_amart furniture pty.pdf")

merged_text = ""
for i in data:
    merged_text += i.text

sllm = llm.as_structured_llm(output_cls=AUCompany)

response = sllm.complete(merged_text)
json_response = json.loads(response.text)
end = timer()
print(json.dumps(json_response,indent=2))
print("\nTime required:")
print(end-start)