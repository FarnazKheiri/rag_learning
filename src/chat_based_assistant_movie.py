from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)


chat = ChatOpenAI(model_name = "gpt-4o-mini", temperature= 0)

template = "You are an assistant that h elps user find info about movies."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

human_message = "Find information about the movie {movie_title}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_message)


chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])


# ## Output of .to_messages():
# [
#     SystemMessage(content="You are an assistant that helps user find info about movies."),
#     HumanMessage(content="Find information about the movie inception")
# ]
# ##%
response = chat.invoke(chat_prompt.format_prompt(movie_title = "inception").to_messages())

print(response.content)