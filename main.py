import ollama
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
import os
import shutil

PROMPT_TEMPLATE = """
You are a helpful assistant answering questions regarding a user's notes in markdown format.
Notes: {notes}

Question: {question}
"""

def load_docs():
    loader = UnstructuredMarkdownLoader()
    docs = loader.load()
    return docs

def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=100, length_function=len, is_separator_regex=False).split_documents(docs)
    return splitter

def embedding_func():
    embeddings = GPT4AllEmbeddings(model_name='all-MiniLM-L6-v2.gguf2.f16.gguf', device='auto', gpt4all_kwargs={}) 
    return embeddings

def build_db(chunks):
    if os.path.exists('chroma'):
        shutil.remove('chroma')
    Chroma.from_documents(chunks, embedding_func(), persist_directory='chroma')

def query_db():
    query = input('How can I help you?: ')
    embedding_func = embedding_func()
    db = Chroma(persist_directory='chroma', embedding_function=embedding_func)
    search = db.similarity_search_with_score(query, k=15)
    context = '\n\n---\n\n'.join([doc.page_content for doc, _score in search])
    return context

