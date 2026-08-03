# Neon Python Study AI Chatbot

import tkinter as tk
from tkinter import messagebox
import random

# --------------------------- KNOWLEDGE BASE ---------------------------

python_topics = {
    "variable": "Variables store data values. Example: name = 'Ancy'",
    "datatype": "Python data types include int, float, string, boolean, list, tuple, set, and dictionary.",
    "loop": "Loops repeat code. Python supports for loops and while loops.",
    "for loop": "for loop repeats through sequences. Example: for i in range(5): print(i)",
    "while loop": "while loop repeats while a condition is True.",
    "function": "Functions are reusable blocks of code. Example: def greet():",
    "list": "Lists store multiple items. Example: fruits = ['apple', 'banana']",
    "dictionary": "Dictionaries store key-value pairs. Example: {'name':'Ancy'}",
    "class": "Classes are blueprints for creating objects.",
    "object": "Objects are instances of classes.",
    "exception": "Exception handling prevents crashes using try and except.",
    "operator": "Operators perform operations like +, -, *, /.",
    "string": "Strings are text data enclosed in quotes.",
    "file": "File handling is used to read and write files.",
}

quiz_questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "answer": "def"
    },
    {
        "question": "Which symbol is used for comments?",
        "answer": "#"
    },
    {
        "question": "Which loop repeats through a sequence?",
        "answer": "for"
    },
    {
        "question": "Which function displays output?",
        "answer": "print"
    }
]

study_plan = """
DAY 1  : Variables and Data Types
DAY 2  : Operators and Input Output
DAY 3  : Conditional Statements
DAY 4  : Loops
DAY 5  : Functions
DAY 6  : Lists and Tuples
DAY 7  : Dictionary and Sets
DAY 8  : File Handling
DAY 9  : Exception Handling
DAY 10 : Mini Project
"""

current_quiz = None
score = 0

# --------------------------- CHATBOT LOGIC ---------------------------


def get_response(user_input):
    global current_quiz
    global score

    user_input = user_input.lower().strip()

    if user_input == "":
        return "Please type something."

    if "hi" in user_input or "hello" in user_input:
        return "Hello! Welcome to Python AI Chatbot ⚡"

    elif "study plan" in user_input or "roadmap" in user_input:
        return study_plan

    elif "quiz" in user_input:
        current_quiz = random.choice(quiz_questions)
        return "⚡ QUIZ TIME ⚡\n\n" + current_quiz["question"]

    elif current_quiz is not None:
        if user_input == current_quiz["answer"].lower():
            score += 1
            current_quiz = None
            return f"✅ Correct! Your score is {score}"
        else:
            answer = current_quiz["answer"]
            current_quiz = None
            return f"❌ Wrong! Correct answer: {answer}"

    elif "score" in user_input:
        return f"🏆 Your score is {score}"

    elif "project" in user_input:
        return """
⚡ Beginner Python Projects ⚡

1. Calculator
2. Quiz App
3. AI Chatbot
4. Face Detection
5. Expense Tracker
6. To-Do List
7. Weather App
"""

    elif "motivation" in user_input:
        return "🔥 Keep coding daily. Small progress creates big success!"

    elif "bye" in user_input:
        return "Goodbye! Keep practicing Python 🚀"

    else:
        for topic in python_topics:
            if topic in user_input:
                return python_topics[topic]

        return "Ask me about variable, loop, function, dictionary, quiz, project, or study plan."


# --------------------------- GUI FUNCTIONS ---------------------------


def send_message():
    user_text = entry.get()

    if user_text.strip() == "":
        messagebox.showwarning("Warning", "Please enter a message")
        return

    chat_box.insert(tk.END, "You: " + user_text + "\n", "user")

    response = get_response(user_text)

    chat_box.insert(tk.END, "Bot: " + response + "\n\n", "bot")

    entry.delete(0, tk.END)
    chat_box.see(tk.END)


# --------------------------- MAIN WINDOW ---------------------------

window = tk.Tk()
window.title("⚡ Python Study AI Chatbot ⚡")
window.geometry("900x700")
window.config(bg="#0a0a0a")

# --------------------------- TITLE ---------------------------

header = tk.Label(
    window,
    text="⚡ PYTHON STUDY AI CHATBOT ⚡",
    font=("Orbitron", 24, "bold"),
    fg="#00ffff",
    bg="#0a0a0a"
)
header.pack(pady=20)

sub_header = tk.Label(
    window,
    text="Learn Python with Interactive AI Assistance",
    font=("Arial", 12, "bold"),
    fg="#ff00ff",
    bg="#0a0a0a"
)
sub_header.pack()

# --------------------------- CHAT FRAME ---------------------------

chat_frame = tk.Frame(window, bg="#00ffff", bd=3)
chat_frame.pack(pady=20)

chat_box = tk.Text(
    chat_frame,
    width=85,
    height=25,
    bg="#111111",
    fg="#39ff14",
    font=("Consolas", 12),
    insertbackground="white",
    wrap=tk.WORD,
    relief=tk.FLAT,
    padx=15,
    pady=15
)
chat_box.pack()

chat_box.tag_config("user", foreground="#00ffff")
chat_box.tag_config("bot", foreground="#ff00ff")

# --------------------------- INPUT FRAME ---------------------------

input_frame = tk.Frame(window, bg="#0a0a0a")
input_frame.pack(pady=10)

entry = tk.Entry(
    input_frame,
    width=55,
    font=("Arial", 14),
    bg="#1a1a1a",
    fg="#ffffff",
    insertbackground="#00ffff",
    relief=tk.FLAT,
    bd=5
)
entry.grid(row=0, column=0, padx=10)

# --------------------------- BUTTONS ---------------------------

send_button = tk.Button(
    input_frame,
    text="SEND",
    command=send_message,
    font=("Arial", 12, "bold"),
    bg="#00ffff",
    fg="black",
    activebackground="#39ff14",
    width=12,
    relief=tk.FLAT,
    cursor="hand2"
)
send_button.grid(row=0, column=1, padx=10)

clear_button = tk.Button(
    input_frame,
    text="CLEAR",
    command=lambda: chat_box.delete("1.0", tk.END),
    font=("Arial", 12, "bold"),
    bg="#ff00ff",
    fg="white",
    activebackground="#ff1493",
    width=12,
    relief=tk.FLAT,
    cursor="hand2"
)
clear_button.grid(row=0, column=2, padx=10)

# --------------------------- FOOTER ---------------------------

footer = tk.Label(
    window,
    text="Built using Python + Tkinter",
    font=("Arial", 10),
    fg="#39ff14",
    bg="#0a0a0a"
)
footer.pack(pady=15)

# --------------------------- DEFAULT MESSAGE ---------------------------

chat_box.insert(tk.END, "Bot: Hello! I am your Neon Python AI Study Assistant ⚡\n", "bot")
chat_box.insert(tk.END, "Bot: Ask about loops, functions, variables, quiz, projects, or study plans.\n\n", "bot")

# --------------------------- RUN WINDOW ---------------------------

window.mainloop()

