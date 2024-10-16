import tkinter as tk
from tkinter import PhotoImage

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Navigation Bars Example")
        self.root.geometry("1300x700")

        # Create a horizontal navigation bar at the top
        self.top_nav_frame = tk.Frame(self.root, bg='lightblue', height=50)
        self.top_nav_frame.pack(side=tk.TOP, fill=tk.X)

        # Add a logo (placeholder for actual image)
        self.logo = tk.Label(self.top_nav_frame, text="Logo", bg='lightblue')
        self.logo.pack(side=tk.LEFT, padx=10)

        # Add a user profile button on the right
        self.user_button = tk.Button(self.top_nav_frame, text="User Profile", command=self.show_user_profile)
        self.user_button.pack(side=tk.RIGHT, padx=10)

        # Create a frame for the vertical navigation bar
        self.nav_frame = tk.Frame(self.root, width=100, bg='lightgrey')
        self.nav_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Add buttons to the vertical navigation bar
        self.button1 = tk.Button(self.nav_frame, text="Home", command=self.show_home)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self.nav_frame, text="About", command=self.show_about)
        self.button2.pack(pady=10)

        self.button3 = tk.Button(self.nav_frame, text="Contact", command=self.show_contact)
        self.button3.pack(pady=10)

        # Create a frame for the main content
        self.content_frame = tk.Frame(self.root, bg='white')
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Initial content
        self.label = tk.Label(self.content_frame, text="Welcome to the Home Page", bg='white')
        self.label.pack(pady=20)

    def show_home(self):
        self.label.config(text="Welcome to the Home Page")

    def show_about(self):
        self.label.config(text="About Us: This is a sample application.")

    def show_contact(self):
        self.label.config(text="Contact Us: email@example.com")

    def show_user_profile(self):
        self.label.config(text="User Profile: User Name")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
