import tkinter as tk
from tkinter import messagebox

from checker import analyze_password
from generator import generate_password


# -----------------------------
# Functions
# -----------------------------

def check_password():

    password = password_entry.get()

    if not password:

        messagebox.showwarning(
            "Password Required",
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

    progress_width = score * 3

    strength_bar.config(
        width=progress_width
    )

    if strength == "WEAK":
        strength_label.config(fg="#e74c3c")

    elif strength == "MEDIUM":
        strength_label.config(fg="#f39c12")

    elif strength == "STRONG":
        strength_label.config(fg="#27ae60")

    else:
        strength_label.config(fg="#16a085")

    if suggestions:

        suggestion_text = "\n".join(
            "• " + suggestion
            for suggestion in suggestions
        )

    else:

        suggestion_text = (
            "✓ Excellent password!\n"
            "✓ No basic security improvements needed."
        )

    suggestions_label.config(
        text=suggestion_text
    )


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


def generate():

    password = generate_password(16)

    password_entry.delete(
        0,
        tk.END
    )

    password_entry.insert(
        0,
        password
    )

    check_password()


def clear():

    password_entry.delete(
        0,
        tk.END
    )

    score_label.config(
        text="Security Score: --/100"
    )

    strength_label.config(
        text="Strength: --",
        fg="#34495e"
    )

    strength_bar.config(
        width=0
    )

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

window.configure(
    bg="#f4f6f7"
)


# -----------------------------
# Header
# -----------------------------

header = tk.Frame(
    window,
    bg="#17202a",
    height=100
)

header.pack(
    fill="x"
)

title = tk.Label(
    header,
    text="🔐 Password Strength Analyzer",
    font=("Arial", 24, "bold"),
    bg="#17202a",
    fg="white"
)

title.pack(
    pady=(22, 5)
)

subtitle = tk.Label(
    header,
    text="Analyze your password security",
    font=("Arial", 11),
    bg="#17202a",
    fg="#d5dbdb"
)

subtitle.pack()


# -----------------------------
# Password input
# -----------------------------

input_frame = tk.Frame(
    window,
    bg="#f4f6f7"
)

input_frame.pack(
    pady=30
)

input_label = tk.Label(
    input_frame,
    text="Enter Password",
    font=("Arial", 13, "bold"),
    bg="#f4f6f7"
)

input_label.pack(
    anchor="w"
)

password_entry = tk.Entry(
    input_frame,
    width=42,
    show="*",
    font=("Arial", 15),
    relief="solid",
    bd=1
)

password_entry.pack(
    side="left",
    pady=10
)

show_button = tk.Button(
    input_frame,
    text="Show",
    command=toggle_password,
    width=7
)

show_button.pack(
    side="left",
    padx=5
)


# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(
    window,
    bg="#f4f6f7"
)

button_frame.pack()

check_button = tk.Button(
    button_frame,
    text="Check Password",
    command=check_password,
    bg="#3498db",
    fg="white",
    font=("Arial", 11, "bold"),
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
    bg="#27ae60",
    fg="white",
    font=("Arial", 11, "bold"),
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
# Result
# -----------------------------

result_frame = tk.Frame(
    window,
    bg="white",
    padx=25,
    pady=20
)

result_frame.pack(
    fill="x",
    padx=40,
    pady=30
)

score_label = tk.Label(
    result_frame,
    text="Security Score: --/100",
    font=("Arial", 17, "bold"),
    bg="white"
)

score_label.pack()

strength_label = tk.Label(
    result_frame,
    text="Strength: --",
    font=("Arial", 20, "bold"),
    fg="#34495e",
    bg="white"
)

strength_label.pack(
    pady=10
)


# Strength bar background

bar_background = tk.Frame(
    result_frame,
    bg="#ecf0f1",
    height=15,
    width=500
)

bar_background.pack()

strength_bar = tk.Frame(
    bar_background,
    bg="#27ae60",
    height=15,
    width=0
)

strength_bar.place(
    x=0,
    y=0
)


# -----------------------------
# Suggestions
# -----------------------------

suggestion_title = tk.Label(
    window,
    text="Security Recommendations",
    font=("Arial", 14, "bold"),
    bg="#f4f6f7"
)

suggestion_title.pack()

suggestions_label = tk.Label(
    window,
    text="",
    justify="left",
    font=("Arial", 11),
    bg="#f4f6f7"
)

suggestions_label.pack(
    pady=10
)


window.mainloop()