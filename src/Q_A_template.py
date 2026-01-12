from langchain_core.prompts.prompt import PromptTemplate
# from langchain_community.llms import HuggingFaceHub
from langchain_huggingface import HuggingFaceEndpoint

prompt_template = PromptTemplate(
    input_variables= ["Question"], 
    template= """ User: {Question}"""
)

my_token = "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"
question = "How old are you?"


hub_llm = HuggingFaceEndpoint(
    repo_id='openai-community/gpt2',
    huggingfacehub_api_token = my_token,
    task="conversational",
)

chain = prompt_template | hub_llm

chain.invoke(question)

