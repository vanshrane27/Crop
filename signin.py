import tkinter as tk
from tkinter import messagebox
import hashlib
import os
import subprocess  # Added import for running main.py

# File to store user credentials
CREDENTIALS_FILE = "user_credentials.txt"


def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def save_credentials(username, password):
    """Saves hashed credentials to a file."""
    with open(CREDENTIALS_FILE, "a") as file:
        file.write(f"{username},{hash_password(password)}\n")


def validate_credentials(username, password):
    """Validates the credentials from the file."""
    if not os.path.exists(CREDENTIALS_FILE):
        return False
    with open(CREDENTIALS_FILE, "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if stored_username == username and stored_password == hash_password(password):
                return True
    return False


def check_username_exists(username):
    """Checks if a username already exists in the file."""
    if not os.path.exists(CREDENTIALS_FILE):
        return False
    with open(CREDENTIALS_FILE, "r") as file:
        for line in file:
            stored_username, _ = line.strip().split(",")
            if stored_username == username:
                return True
    return False


def switch_to_signup():
    """Switch to Sign-Up page."""
    login_frame.pack_forget()
    signup_frame.pack()


def switch_to_signin():
    """Switch to Sign-In page."""
    signup_frame.pack_forget()
    login_frame.pack()


def signup():
    """Handle Sign-Up logic."""
    username = entry_signup_username.get()
    password = entry_signup_password.get()
    confirm_password = entry_signup_confirm_password.get()

    if not username or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    if check_username_exists(username):
        messagebox.showerror("Error", "Username already exists!")
        return

    save_credentials(username, password)
    messagebox.showinfo("Success", "Account created successfully!")
    switch_to_signin()


def signin():
    """Handle Sign-In logic."""
    username = entry_signin_username.get()
    password = entry_signin_password.get()

    if validate_credentials(username, password):
        #Smessagebox.showinfo("Success", "Login successful!")
        # Run main.py
        root.destroy()  # Close the current window
        subprocess.run(["python", "dash.py"])  # Ensure main.py is in the same directory
    else:
        messagebox.showerror("Error", "Invalid username or password!")


# Tkinter Window
root = tk.Tk()
root.title("Sign-In & Sign-Up")
root.geometry("1300x700")

# Sign-In Frame
login_frame = tk.Frame(root)

tk.Label(login_frame, text="Sign-In", font=("Arial", 18)).pack(pady=10)
tk.Label(login_frame, text="Username").pack()
entry_signin_username = tk.Entry(login_frame)
entry_signin_username.pack()

tk.Label(login_frame, text="Password").pack()
entry_signin_password = tk.Entry(login_frame, show="*")
entry_signin_password.pack()

tk.Button(login_frame, text="Login", command=signin).pack(pady=10)
tk.Button(login_frame, text="Create an Account", command=switch_to_signup).pack()

# Sign-Up Frame
signup_frame = tk.Frame(root)

tk.Label(signup_frame, text="Sign-Up", font=("Arial", 18)).pack(pady=10)
tk.Label(signup_frame, text="Username").pack()
entry_signup_username = tk.Entry(signup_frame)
entry_signup_username.pack()

tk.Label(signup_frame, text="Password").pack()
entry_signup_password = tk.Entry(signup_frame, show="*")
entry_signup_password.pack()

tk.Label(signup_frame, text="Confirm Password").pack()
entry_signup_confirm_password = tk.Entry(signup_frame, show="*")
entry_signup_confirm_password.pack()

tk.Button(signup_frame, text="Sign Up", command=signup).pack(pady=10)
tk.Button(signup_frame, text="Already have an account?", command=switch_to_signin).pack()

# Start with Sign-In Frame
login_frame.pack()

# Run the application
root.mainloop()
