# File: app.py
import json
import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Load intents
with open('intents.json') as file:
    intents = json.load(file)

# Function to get bot response
def get_response(user_input):
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return random.choice(intent['responses'])
    return "I'm sorry, I don't understand that. Can you rephrase?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def chatbot_response():
    user_message = request.args.get('msg')  # Get user input from frontend
    bot_response = get_response(user_message)
    return bot_response

if __name__ == "__main__":
    app.run(debug=True)
