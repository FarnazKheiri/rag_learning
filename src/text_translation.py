from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI


llm = ChatOpenAI (model_name = "gpt-4o-mini", temperature= 0)

prompt_template = PromptTemplate(input_variables= ["source_language", "target_language", "text"],
                                  template= "Please translate the following text from {source_language} to {target_language}: {text}")

text = "How are you doing today?"
source_language = "English"
target_language = "French" 

translated_chain = prompt_template | llm

response = translated_chain.invoke({
    "source_language": source_language, 
    "target_language": target_language, 
    "text": text
})
print(response.content)
