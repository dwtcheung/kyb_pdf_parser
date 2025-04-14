# KYB PDF Parser
This is a demo repo of how to use Ollama locally hosted LLM to parse Company Profile PDF and return as a JSON object.

The demo is split into two parts:
  1. Parsing PDF that contains text and structure using Llama Index structured output
  2. Parsing PDF that is actually an image (no markdown can be generated) using Ollam OCR and Llama Index structured output

The general approach as follows:
* Manually review the PDF format and create a Pydantic base model
* Load the PDF as markdown
* Create a structured llm object, ask it to complete

## Dependancies
1. Ollama installed locally with Embed, Vision, and general models installed
2. llama_index, pymupdf4llm, and ollama_ocr Python libraries

## Note about performance
* Accuracy of Ollam OCR is a bit suspect and different LLM will generate different results
* It is entirely possible to get better results using bigger models or cloud base LLM but there is privacy concern since the data contains name, address, DOB, and/or national ID numbers
