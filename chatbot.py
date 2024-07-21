#importing required libraries 

import tkinter as tk
from tkinter import scrolledtext
import random

#creating a set of rules for chatbot responses using classes and objects 

class Chatbot:
    def __init__(self):
        self.responses = {
            "hi": ["Hello!", "Hi there!", "Greetings!", "Howdy!"],
            "hello" : ["Hi there!!"],
            "how are you": ["I'm just a bot, but thanks for asking!", "Doing great, how about you?"],
            "bye": ["Goodbye!", "See you later!", "Take care!"],
            "default": ["I'm not sure how to respond to that.", "Can you rephrase that?","i apologise im not trained on advance level "]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        return random.choice(self.responses["default"])


# setting up GUi for the chatbot using tkinter module 

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        
        self.chatbot = Chatbot()

        self.chat_area = scrolledtext.ScrolledText(root, state='disabled', wrap='word')
        self.chat_area.grid(row=0, column=0, columnspan=2)

        self.user_input = tk.Entry(root, width=80)
        self.user_input.grid(row=1, column=0)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1)

    def send_message(self):
        user_message = self.user_input.get()
        if user_message:
            self.update_chat_area("You: " + user_message)
            response = self.chatbot.get_response(user_message)
            self.update_chat_area("Bot: " + response)
            self.user_input.delete(0, tk.END)

    def update_chat_area(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + '\n')
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)  # Scroll to the end

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()