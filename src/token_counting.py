from langchain_openai import ChatOpenAI
from langchain_community.callbacks import get_openai_callback

# two distinct responses for the same prompt.
llm = ChatOpenAI(model= "gpt-4o-mini", n = 2)

with get_openai_callback() as cb:
    print(llm.invoke("Tell me a joke"))
    print(cb)


