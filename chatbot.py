import json
import random
import streamlit as st
from transformers import pipeline

# Load intents from JSON
def load_intents():
    with open("intents.json", "r") as file:
        data = json.load(file)
    return data["intents"]

# Get a response based on user input
def get_response(user_input, intents):
    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input.lower():
                return random.choice(intent["responses"])
    return "I'm sorry, I didn't understand that. Could you rephrase?"

# Streamlit app
def chatbot_app():
    st.title("FAQ Chatbot")
    st.write("Ask me anything about our services!")

    # Load intents
    intents = load_intents()

    # User input
    user_input = st.text_input("You:", "")
    if user_input:
        response = get_response(user_input, intents)
        st.write(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot_app()
