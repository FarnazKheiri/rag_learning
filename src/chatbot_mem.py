from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
    AIMessage
)

llm = ChatOpenAI(model_name= "gpt-4o-mini", temperature= 0)

messages =  [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of France?"),
    # AIMessage(content= "The capital of France is Paris.")

]

prompt = HumanMessage (content= "I'd like to know more about the city you just mentioned")

messages.append(prompt)

chat = llm.invoke(messages)

print(chat.content)

