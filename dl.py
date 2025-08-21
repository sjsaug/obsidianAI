from ollama import chat

def inference(model):
    msg = input("Inquiry: ")
    response = chat(model, msg);
    return response['message']['content']