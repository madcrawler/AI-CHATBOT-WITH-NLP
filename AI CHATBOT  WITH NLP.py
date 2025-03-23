import nltk
import random
import string
import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK resources
nltk.download("punkt")
nltk.download("stopwords")

# Define chatbot responses
pairs = [
    [r"(hi|hello|hey)", ["Hello!", "Hey there!", "Hi! How can I help you?"]],
    [r"(how are you|how do you do|how's it going)", ["I'm just a chatbot, but I'm doing great! How about you?"]],
    [r"(what is your name|who are you)", ["I'm an AI chatbot, here to assist you."]],
    [r"(what can you do)", ["I can answer your questions, chat with you, and help with basic queries."]],
    [r"(bye|goodbye)", ["Goodbye!", "See you later!", "Have a great day!"]],
    [r"(.*)", ["I'm not sure how to respond to that. Can you rephrase?"]],
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

# Preprocess user input
def process_input(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)

    # Keep stopwords in case they are essential (e.g., "how are you")
    stop_words = set(stopwords.words("english"))

    # Only remove stopwords if they are not forming essential phrases
    tokens = [word for word in tokens if word not in string.punctuation]

    return " ".join(tokens)

# Get chatbot response
def chatbot_response(user_input):
    processed_input = process_input(user_input)
    response = chatbot.respond(processed_input)
    return response if response else "I'm not sure how to respond to that."

# Function to handle sending messages
def send_message():
    user_input = user_entry.get()
    if user_input.strip() == "":
        return  # Don't send empty messages

    chat_display.insert(tk.END, "You: " + user_input + "\n", "user")
    response = chatbot_response(user_input)
    chat_display.insert(tk.END, "Chatbot: " + response + "\n", "bot")

    user_entry.delete(0, tk.END)  # Clear input field
    chat_display.yview(tk.END)  # Auto-scroll to latest message

# GUI Setup
root = tk.Tk()
root.title("Chatbot")

# Chat Display Area
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_display.pack(padx=10, pady=10)
chat_display.tag_config("user", foreground="blue")
chat_display.tag_config("bot", foreground="green")

# Input Field
user_entry = tk.Entry(root, width=50, font=("Arial", 12))
user_entry.pack(padx=10, pady=5)
user_entry.bind("<Return>", lambda event: send_message())  # Send message on Enter key

# Send Button
send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(pady=5)

# Start Chatbot GUI
root.mainloop()
