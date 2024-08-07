import ollama
from langchain_community.embeddings import gpt4all
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma

PROMPT_TEMPLATE = """
You are a helpful assistant answering questions regarding a user's notes in markdown format.
Notes: {notes}

Question: {question}
"""