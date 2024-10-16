import tkinter as tk

class StartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Get Started Example")
        self.root.geometry("1300x700")

        # Create a frame to center the button
        self.center_frame = tk.Frame(self.root)
        self.center_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Create the Get Started button
        self.get_started_button = tk.Button(self.center_frame, text="Get Started", font=("Arial", 24), command=self.get_started)
        self.get_started_button.pack(pady=20)

    def get_started(self):
        # Action to be performed when the button is clicked
        print("Get Started button clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = StartApp(root)
    root.mainloop()
