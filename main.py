import ollama
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
import os
import shutil

macos_fix = False
if macos_fix == True:
    # do not use, not recommended due for security. only using because it fixes a bug i have.
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

PROMPT_TEMPLATE = """
You are a helpful assistant answering questions regarding a user's notes in markdown format.
Notes: {notes}

Question: {question}
"""
MODEL = 'llama3.1'
NOTES_PATH = 'data/'

def load_docs():
    docs = []
    for filename in os.listdir(NOTES_PATH):
        if filename.endswith('.md'):
            file_path = os.path.join(NOTES_PATH, filename)
            loader = UnstructuredMarkdownLoader(file_path)
            docs.extend(loader.load())
    return docs

def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=100, length_function=len, is_separator_regex=False).split_documents(docs)
    return splitter

def embedding_func():
    embeddings = GPT4AllEmbeddings(model_name='all-MiniLM-L6-v2.gguf2.f16.gguf', device='gpu', gpt4all_kwargs={}) 
    return embeddings

def build_db(chunks: list[Document]):
    if os.path.exists('chroma'):
        shutil.remove('chroma')
        Chroma.from_documents(chunks, embedding_func(), persist_directory='chroma')

def query_db(embedding_func):
    query = input('How can I help you?: ')
    db = Chroma(persist_directory='chroma', embedding_function=embedding_func)
    search = db.similarity_search_with_score(query, k=15)
    context = '\n\n---\n\n'.join([doc.page_content for doc, _score in search])
    return query, context

def inference(context, query):
    response = ollama.chat(
        model=MODEL,
        messages=[{'role': 'user', 'content': ChatPromptTemplate.from_template(PROMPT_TEMPLATE).format(notes=context, question=query)}],
        stream=True,
        )
    for chunk in response:
        print(chunk['message']['content'], end='', flush=True)

if __name__ == '__main__':
    docs = load_docs()
    chunks = split_docs(docs)
    build_db(chunks)
    embedding_func = embedding_func()
    query, context = query_db(embedding_func)
    inference(context, query)