from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate

# Define the prompt
template = """
You are a helpful assistant. Answer the following question as best you can.

Here is the conversation so far: {Context}
Question: {input}
Answer:
"""

# Use the chat model
model = ChatOllama(model="llama3")

# Set up the prompt template
prompt = PromptTemplate.from_template(template)

# Pipe prompt output into the model
chain = prompt | model

# Generate response
def generate_response(context, user_input):
    return chain.invoke({"Context": context, "input": user_input})

# Chat loop
def handle_conversation():
    context = ""
    print("Welcome to the AI ChatBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = generate_response(context, user_input)
        text = response.content if hasattr(response, "content") else str(response)
        print("Bot:", text)
        context += f"\nUser: {user_input}\nAI: {text}"

if __name__ == "__main__":
    handle_conversation()
