import tkinter as tk
import re

def password_strength_checker(password):
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1

    # Check for digits
    if re.search(r'[0-9]', password):
        score += 1

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    # Determine strength level
    if score == 1:
        strength = "Very Weak"
    elif score == 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    elif score == 5:
        strength = "Very Strong"
    else:
        strength = "Please enter a valid password"

    return strength

def check_password():
    password = password_entry.get()
    strength = password_strength_checker(password)
    result_label.config(text=f"Password Strength: {strength}")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the widgets
tk.Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=0, column=1, padx=10, pady=10)

check_button = tk.Button(root, text="Check Strength", command=check_password)
check_button.grid(row=1, columnspan=2, pady=10)

result_label = tk.Label(root, text="Password Strength: ")
result_label.grid(row=2, columnspan=2, pady=10)

# Run the application
root.mainloop()
