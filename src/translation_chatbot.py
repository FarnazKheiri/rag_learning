from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

chat = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# messages = [
# 	SystemMessage(content="You are a helpful assistant that translates English to French."),
# 	HumanMessage(content="Translate the following sentence: I love programming.")
# ]

# print(chat.invoke(messages).content)


batch_messages = [
  [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="Translate the following sentence: I love programming.")
  ],
  [
    SystemMessage(content="You are a helpful assistant that translates French to English."),
    HumanMessage(content="Translate the following sentence: J'aime la programmation.")
  ],
]

print(chat.generate(batch_messages))