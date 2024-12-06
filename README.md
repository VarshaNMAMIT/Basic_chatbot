## Basic_chatbot
Implementation of a Basic Chatbot using NLP
This project is a chatbot built using Natural Language Processing (NLP) techniques to handle user queries and provide meaningful responses. The chatbot is designed to simulate human-like conversations by processing input and returning appropriate responses based on predefined intents. This project is built with Flask as the backend framework, and it uses pattern matching for recognizing user input.


# Features
Handles various user inputs like greetings and general conversation.

Built using Python and Flask framework.

JSON-based intent structure to allow easy modification and expansion of chatbot capabilities.

Responses are selected randomly from a predefined set to make interactions more dynamic.

Logs user and bot interactions to a CSV file for further analysis.


## Table of Contents
- **[Usage](#usage)**
- **[Folder Structure](#folder-structure)**
- **[Technologies Used](#technologies-used)**
- **[How it Works](#how-it-works)**

# Usage
Once the environment is set up, you can run the chatbot locally by starting the Flask server:

python app.py

After running the command, the Flask app will be hosted locally, and you can access it via:

http://localhost:5000

How to Interact:

Open the application in your web browser.

Enter a message in the chatbot interface, and it will provide a response based on predefined patterns.

Check the chatbot_log.csv file for a log of all interactions.

# Folder structure:
#### chatbot-nlp/
#### ├── app.py                # Main Python file to run the Flask app
#### ├── intents.json          # JSON file containing predefined intents, patterns, and responses
#### ├── chatbot_log.csv       # Log file to record user-bot interactions
#### ├── requirements.txt      # Python dependencies for the project
#### └── templates/└── index.html  # HTML file for the chatbot interface
#### └── static/└── style.css 
    
# Technologies Used
Python: The main programming language.

Flask: Lightweight web framework for the backend.

JSON: Used for storing intents, patterns, and responses.

CSV: Used for logging chatbot interactions.

HTML: Simple front-end interface for user interaction with the chatbot.

# How It Works
**Intent Recognition:** The chatbot processes user input and checks if it matches any predefined patterns in the intents.json file.

**Random Response Generation:** Once a match is found, the chatbot randomly selects a response from the corresponding set of responses and presents it to the user.

**Logging Interactions:** Each interaction between the user and the bot is logged in a CSV file for later analysis.
The chatbot doesn't rely on advanced NLP models like machine learning-based intent classifiers; instead, it uses simple pattern matching to recognize user input


![image](https://github.com/user-attachments/assets/fe045dc0-de9c-406a-ad46-a90886b5809c)


