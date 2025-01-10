import tkinter as tk
from tkinter import PhotoImage
import subprocess
import sys

class StartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Get Started Example")
        self.root.geometry("1300x700")
        self.root.configure(bg="#21443d")  # Set background color (light blue)
        self.root.resizable(False, False)

        # Create a frame to center the button
        self.center_frame = tk.Frame(self.root, bg="#21443d")
        self.center_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Load and display the logo above the button with x and y axis positioning
        self.logo = PhotoImage(file="logo.png")  # Path to your logo image
        self.logo_label = tk.Label(self.root, image=self.logo, bg="#21443d")

        # Set x and y axis for logo positioning
        self.logo_label.place(x=390, y=30)  # Adjust x and y as needed

        # Create the Get Started button
        self.get_started_button = tk.Button(self.root, text="Get Started", font=("Arial", 24), command=self.get_started,bg="#89b42e", fg="white", activebackground="darkgreen",activeforeground="white")

        # Set x and y axis for button positioning
        self.get_started_button.place(x=550, y=530)  # Adjust x and y as needed

    def get_started(self):
        # Destroy the current window and open the next page
        self.root.destroy()
        subprocess.Popen([sys.executable, "signin.py"])  # Use sys.executable to ensure correct Python interpreter

if __name__ == "__main__":
    root = tk.Tk()
    app = StartApp(root)
    root.mainloop()
