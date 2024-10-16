import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1300x700")

        # Create a frame for the top section with logo
        self.top_frame = tk.Frame(self.root, bg='lightblue', height=50)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        # Add a logo (placeholder for actual image)
        self.logo = tk.Label(self.top_frame, text="Logo", bg='lightblue', font=("Arial", 16))
        self.logo.pack(side=tk.LEFT, padx=10)

        # Create a frame for the login form
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=50)

        # Username label and entry
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password label and entry
        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.login_frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Login button
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2, pady=10)

        # Register button
        self.register_button = tk.Button(self.login_frame, text="Register", command=self.register)
        self.register_button.grid(row=3, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Here you would typically validate the username and password
        if username and password:
            messagebox.showinfo("Login", "Login successful!")
        else:
            messagebox.showwarning("Login", "Please enter username and password.")

    def register(self):
        messagebox.showinfo("Register", "Registration page not implemented yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
