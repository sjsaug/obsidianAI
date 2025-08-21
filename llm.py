from ollama import chat
from langchain.prompts import ChatPromptTemplate

PROMPT_TEMPLATE = """
You are reviewing the results from exploratory data analysis of a dataset. Please summarize the results.
Shape: {shape}
Missing Values {mvs}
Summary Statistics: {stats}
"""

def inference(model, shape, mvs, stats):
    response = chat(
        model=model,
        messages=[{'role': 'user', 'content': ChatPromptTemplate.from_template(PROMPT_TEMPLATE).format(shape=shape, mvs=mvs, stats=stats)}],
        stream=True,
        )
    for chunk in response:
        print(chunk['message']['content'], end='', flush=True)