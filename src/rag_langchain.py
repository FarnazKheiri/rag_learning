from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(model= "gpt-3.5-turbo-instruct", temperature= 0.9)

# text = "Suggest a personalized workout routine for someone looking to improve cardiovascular endurance and prefers outdoor activities."
# print(llm(text))

prompt = PromptTemplate(
    input_variables = ["product"],
    template= "What is a good name for a company that makes {product}?" 
)

chain = LLMChain(llm= llm , prompt= prompt )

print(chain.run("eco-friendly water bottles"))


