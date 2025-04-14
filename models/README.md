# Model Creation Instructions

When creating a Python Pydantic model to match the company profile data, you need to define every single attribute as Key name in the Pydantic class model. Failing to due so may confuse the LLM during data extraction. For values that may be blank, use the Optional type. 
