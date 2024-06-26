import tkinter as tk
from tkinter import messagebox
import random
import os

# Function to list the files containing all the methods
def list_files_in_methods_folder():
    methods_folder = 'methods'
    try:
        files = [f"{methods_folder}/{file}" for file in os.listdir(methods_folder) if file.endswith('.txt')]
        if not files:
            messagebox.showwarning("No Files", "No .txt files found in the methods folder.")
        return files
    except FileNotFoundError:
        messagebox.showerror("Error", f"The folder '{methods_folder}' does not exist.")
        return []

# Function to check the user's input
def check_answers():
    correct = True
    errors = 0
    for i, entry in enumerate(entries):
        if entry.get().strip().replace(" ", "") != missing_words[i].replace(" ", ""):
            errors += 1
            correct = False
            entry.config(background="red")
        else:
            entry.config(background="green")
    if correct:
        messagebox.showinfo("Result", "Congratulations! All answers are correct.")
    else:
        messagebox.showerror("Result", f"Some answers are incorrect ({errors}). Please try again.")
        
# Function to display solutions
def display_solutions():
    text_area.config(state=tk.NORMAL)
    for i, entry in enumerate(entries):
        entry.delete(0, tk.END)
        entry.insert(0, missing_words[i])
    text_area.config(state=tk.DISABLED)

# Function to load the text from a file
def load_text_from_file():
    with open(files[random.randint(0, len(files) - 1)], 'r') as file:
        lines = file.readlines()
    process_text(lines)

# Function to process the text and create the UI elements
def process_text(lines):
    global entries, missing_words
    entries = []
    missing_words = []
    text_area.config(state=tk.NORMAL)
    text_area.delete("1.0", tk.END)
    
    for line in lines:
        if '#' in line:
            words_part = line.split('#')[1]
            words = words_part.strip()
        else:
            text_part, words = line, []

        parts = text_part.split("___")
        for i, part in enumerate(parts):
            text_area.insert(tk.END, part)
            if i < len(parts) - 1:
                entry = tk.Entry(text_area, width=int(text_area.winfo_width()*0.05), foreground="black", relief="solid", borderwidth=1, font=("Ariel", 12))
                text_area.window_create(tk.END, window=entry)
                entries.append(entry)
                
        if type(words) == str:
            missing_words.append(words)

    text_area.config(state=tk.DISABLED)
    
# Get the list of files in the methods folder
files = list_files_in_methods_folder()

# Create the main window
root = tk.Tk()
root.title("Completa gli scheletri")

# Get the width and height of the main window
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Set the window dimensions
root.state("zoomed")

# Create a frame for the text and entries
frame = tk.Frame(root, highlightbackground="red", highlightthickness=1, bd=0)
frame.pack(side="top", padx=10, pady=10)

# Create a Text widget for displaying the text
text_area = tk.Text(frame, font=("Ariel", 12), width=int(width*0.08), height=int(height*0.05))
text_area.pack()

# Create a button to load the text from a file
load_button = tk.Button(root, text="Next Method", command=load_text_from_file)
load_button.pack(side="left", padx=10, pady=10)

# Create a button to check the answers
check_button = tk.Button(root, text="Check Answers", command=check_answers)
check_button.pack(side="left", padx=10, pady=10)

# Create a button to solve the exercise
solve_button = tk.Button(root, text="Solve Exercise", command=display_solutions)
solve_button.pack(side="left", padx=10, pady=10)

# Run the application
root.mainloop()
