from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_openai import ChatOpenAI
# from langchain.chains import LLMChain

## 1
examples = [
{"quary": "What's the weather like?",
 "answer": "It's raining cats and dogs, better bring an umbrella!"},
 {"quary": "How old are you?",
  "answer": "Age is just a number, but I'm timeless."}
]

#####
example_template = """
user: {quary}
AI: {answer}
"""

prompt_template = PromptTemplate(
    input_variables= ["quary", "answer"],
    template= example_template
)
#####

#### # the prefix is our instructions
prefix = """The following are excerpts from conversations with an AI
assistant. The assistant is known for its humor and wit, providing
entertaining and amusing responses to users' questions. Here are some
examples:
"""

# the suffix our user input and output indicator
suffix = """
User: {quary}
AI: 
"""
#####


few_shot_prompt_template = FewShotPromptTemplate(
examples = examples,
example_prompt = prompt_template,
prefix = prefix,
suffix = suffix,
input_variables=["query"],
example_separator="\n\n"
)



llm = ChatOpenAI (model_name = "gpt-4o-mini", temperature= 0)

# | takes the output of the element on the left and passes it as the input to the element on the right.
chain = few_shot_prompt_template | llm

print(chain.invoke("What's the meaning of life?"))
