import tkinter as tk
from tkinter import messagebox

from checker import analyze_password
from generator import generate_password


# -----------------------------
# Check Password
# -----------------------------

def check_password():

    password = password_entry.get()

    if not password:
        messagebox.showwarning(
            "Warning",
            "Please enter a password."
        )
        return

    score, strength, suggestions = analyze_password(password)

    score_label.config(
        text=f"Security Score: {score}/100"
    )

    strength_label.config(
        text=f"Strength: {strength}"
    )

    # Strength bar
    bar_width = int(score * 4)

    strength_bar.config(width=bar_width)

    # Suggestions
    if suggestions:

        suggestion_text = "\n".join(
            "• " + item
            for item in suggestions
        )

        suggestions_label.config(
            text="Suggestions:\n" + suggestion_text
        )

    else:

        suggestions_label.config(
            text="✓ No major weaknesses detected."
        )


# -----------------------------
# Show / Hide Password
# -----------------------------

def toggle_password():

    if password_entry.cget("show") == "*":

        password_entry.config(show="")

        show_button.config(
            text="Hide"
        )

    else:

        password_entry.config(show="*")

        show_button.config(
            text="Show"
        )


# -----------------------------
# Generate Password
# -----------------------------

def generate():

    password = generate_password(16)

    password_entry.delete(0, tk.END)

    password_entry.insert(0, password)

    check_password()


# -----------------------------
# Clear
# -----------------------------

def clear():

    password_entry.delete(0, tk.END)

    score_label.config(
        text="Security Score: 0/100"
    )

    strength_label.config(
        text="Strength: -"
    )

    strength_bar.config(width=0)

    suggestions_label.config(
        text=""
    )


# -----------------------------
# Main Window
# -----------------------------

window = tk.Tk()

window.title(
    "Password Strength Analyzer"
)

window.geometry(
    "650x650"
)

window.resizable(
    False,
    False
)


# -----------------------------
# Header
# -----------------------------

header = tk.Frame(
    window,
    bg="#1f2937",
    height=100
)

header.pack(
    fill="x"
)

title = tk.Label(
    header,
    text="Password Strength Analyzer",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#1f2937"
)

title.pack(
    pady=(20, 5)
)

subtitle = tk.Label(
    header,
    text="Analyze and generate secure passwords",
    font=("Arial", 11),
    fg="white",
    bg="#1f2937"
)

subtitle.pack()


# -----------------------------
# Password Label
# -----------------------------

password_label = tk.Label(
    window,
    text="Enter Password",
    font=("Arial", 14, "bold")
)

password_label.pack(
    pady=(30, 10)
)


# -----------------------------
# Password Entry
# -----------------------------

password_frame = tk.Frame(window)

password_frame.pack()


password_entry = tk.Entry(
    password_frame,
    width=35,
    font=("Arial", 14),
    show="*"
)

password_entry.pack(
    side="left",
    padx=5
)


show_button = tk.Button(
    password_frame,
    text="Show",
    command=toggle_password
)

show_button.pack(
    side="left"
)


# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(window)

button_frame.pack(
    pady=25
)


check_button = tk.Button(
    button_frame,
    text="Check Password",
    command=check_password,
    width=18
)

check_button.grid(
    row=0,
    column=0,
    padx=5
)


generate_button = tk.Button(
    button_frame,
    text="Generate Secure",
    command=generate,
    width=18
)

generate_button.grid(
    row=0,
    column=1,
    padx=5
)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear,
    width=10
)

clear_button.grid(
    row=0,
    column=2,
    padx=5
)


# -----------------------------
# Score
# -----------------------------

score_label = tk.Label(
    window,
    text="Security Score: 0/100",
    font=("Arial", 18, "bold")
)

score_label.pack(
    pady=10
)


# -----------------------------
# Strength
# -----------------------------

strength_label = tk.Label(
    window,
    text="Strength: -",
    font=("Arial", 16)
)

strength_label.pack(
    pady=5
)


# -----------------------------
# Strength Bar
# -----------------------------

strength_bar = tk.Label(
    window,
    text="",
    bg="green",
    height=1,
    width=0
)

strength_bar.pack(
    pady=10
)


# -----------------------------
# Suggestions
# -----------------------------

suggestions_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    justify="left",
    wraplength=550
)

suggestions_label.pack(
    pady=20
)


# -----------------------------
# Start Application
# -----------------------------

window.mainloop()