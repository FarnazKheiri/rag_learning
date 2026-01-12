from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI


llm = ChatOpenAI (model_name = "gpt-4o-mini", temperature= 0)

prompt_template = PromptTemplate(input_variables= ["text"],
                                 template= "Summarize the following text to one sentence: {text}" )

summarization_chain = prompt_template | llm

summarized_text = summarization_chain.invoke("LangChain provides many modules that can be used to build language model applications. Modules can be combined to create more complex applications, or be used individually for simple applications. The most basic building block of LangChain is calling an LLM on some input. Let’s walk through a simple example of how to do this. For this purpose, let’s pretend we are building a service that generates a company name based on what the company makes.")


print(summarized_text.content)
