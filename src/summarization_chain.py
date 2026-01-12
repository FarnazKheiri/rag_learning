from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.chains.summarize import load_summarize_chain


llm = ChatOpenAI(model_name = "gpt-4o-mini", temperature= 0)


summarization_model = load_summarize_chain(llm)

document_loader = PyPDFLoader(file_path= r"C:\Users\Farnaz\rag_learning\s41237-016-0008-2 (1).pdf")
document = document_loader.load()

summary = summarization_model(document)
print(summary)