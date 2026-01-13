import requests
from newspaper import Article
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI




# headers (The "Fake Identity"): When a script visits a website, many sites block it if they realize it's a bot. By setting a User-Agent, the script "disguises" itself as a standard Google Chrome browser running on Windows,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

article_url = "https://www.artificialintelligence-news.com/news/meta-claims-new-ai-supercomputer-will-set-records/"

session = requests.Session()


## This line goes to the URL and asks the server for the HTML code.
response = session.get(article_url, headers=headers, timeout= 10)

if response.status_code == 200:

    # creating an Instance of that class.
    # The input article_urls tells this container (article) exactly which "house" (webpage) it needs to go to.
    article = Article(article_url)

    # fetches the HTML from the URL.
    article.download()

    # analyzes the HTML, finds the headline, ignores the navigation menus, ads, and footer links, and isolates the actual story text.
    article.parse()

    # print(f"title: {article.title}")
    # print(f"Text: {article.text}")


article_title = article.title
article_text = article.text


llm = ChatOpenAI (model_name = "gpt-4o-mini", temperature= 0)

# prompt_template = PromptTemplate(input_variables= ["article"],
#                template= "summarize this {article}")


# summarization_chain = prompt_template | llm
# text = summarization_chain.invoke(article_text)

# print(text.content)



message_template = """You are an advanced AI assistant that summarizes online articles into bulleted lists in French.


======================
Title: {article_title}


{article_text}
======================
"""

message_prompt = message_template.format(article_text = article_text, article_title = article_title)

message = HumanMessage(content= message_prompt)

response = llm.invoke([message])

print(response)