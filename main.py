import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os
import subprocess

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Navigation Bars Example")
        self.root.geometry("1300x700")
        self.root.resizable(False, False)

        # Create a horizontal navigation bar at the top
        self.top_nav_frame = tk.Frame(self.root, bg='#21443d', height=50)
        self.top_nav_frame.pack(side=tk.TOP, fill=tk.X)

        # Add a logo (placeholder for actual image)
        original_logo = Image.open("logo.png")  # Replace with the actual path to your PNG logo
        self.logo_image = original_logo.resize((60, 60), Image.LANCZOS)  # Resize to desired width and height
        self.logo_image = ImageTk.PhotoImage(self.logo_image)  # Convert to PhotoImage

        self.logo = tk.Label(self.top_nav_frame, image=self.logo_image, bg='#21443d')
        self.logo.pack(side=tk.LEFT, padx=10)

        # Add a user profile button on the right
        self.user_button = tk.Button(self.top_nav_frame, text="User Profile", command=self.show_user_profile)
        self.user_button.pack(side=tk.RIGHT, padx=10)

        # Create a frame for the vertical navigation bar
        self.nav_frame = tk.Frame(self.root, width=100, bg='#2b803f')
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
        # Clear any existing content
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Add a welcome label
        welcome_label = tk.Label(self.content_frame, text="Welcome to the Home Page", bg='white', font=("Arial", 18))
        welcome_label.pack(pady=20)

        # Create a frame for the search bar and button
        search_frame = tk.Frame(self.content_frame, bg='white')
        search_frame.pack(pady=20)

        # Add a search bar
        search_entry = tk.Entry(search_frame, width=30, font=("Arial", 14))
        search_entry.pack(side=tk.LEFT, padx=10)

        # Add a submit button
        def handle_search():
            search_query = search_entry.get()
            print(f"Search query: {search_query}")  # Replace with desired functionality

        search_button = tk.Button(search_frame, text="Submit", command=handle_search)
        search_button.pack(side=tk.LEFT)

        # Add the Yield Prediction button below
        def open_yield_prediction():
            self.root.destroy()  # Close the current window
            subprocess.run(["python", "crop_yield_prediction.py"])  # Replace with the path to your script if needed

        yield_button = tk.Button(self.content_frame, text="Yield Prediction", font=("Arial", 14), command=open_yield_prediction)
        yield_button.pack(pady=20)

    def show_about(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        welcome_label = tk.Label(self.content_frame, text="...", bg='white', font=("Arial", 18))
        welcome_label.pack(pady=20)

    def show_contact(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        welcome_label = tk.Label(self.content_frame, text="Contact Us: email@example.com", bg='white', font=("Arial", 18))
        welcome_label.pack(pady=20)

    def show_user_profile(self):
        self.label.config(text="User Profile: User Name")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
