import tkinter as tk
from tkinter import messagebox

class RegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Page")
        self.root.geometry("1300x700")

        # Create a frame for the top section with logo
        self.top_frame = tk.Frame(self.root, bg='lightblue', height=50)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        # Add a logo (placeholder for actual image)
        self.logo = tk.Label(self.top_frame, text="Logo", bg='lightblue', font=("Arial", 16))
        self.logo.pack(side=tk.LEFT, padx=10)

        # Create a frame for the registration form
        self.registration_frame = tk.Frame(self.root)
        self.registration_frame.pack(pady=50)

        # Username label and entry
        self.username_label = tk.Label(self.registration_frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.registration_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password label and entry
        self.password_label = tk.Label(self.registration_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.registration_frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Confirm Password label and entry
        self.confirm_password_label = tk.Label(self.registration_frame, text="Confirm Password:")
        self.confirm_password_label.grid(row=2, column=0, padx=10, pady=10)
        self.confirm_password_entry = tk.Entry(self.registration_frame, show='*')
        self.confirm_password_entry.grid(row=2, column=1, padx=10, pady=10)

        # Register button
        self.register_button = tk.Button(self.registration_frame, text="Register", command=self.register)
        self.register_button.grid(row=3, columnspan=2, pady=10)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Basic validation
        if username and password:
            if password == confirm_password:
                messagebox.showinfo("Register", "Registration successful!")
                # Here you would typically save the user data
            else:
                messagebox.showwarning("Register", "Passwords do not match.")
        else:
            messagebox.showwarning("Register", "Please fill in all fields.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationApp(root)
    root.mainloop()
