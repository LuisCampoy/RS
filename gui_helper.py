import tkinter as tk
from tkinter import ttk
import threading
import time
import sys
import io
from main import main

# Flag to control the execution of the long-running task
stop_flag = threading.Event()

def long_running_task():
    while not stop_flag.is_set():
        print("Script is running")
        #time.sleep(1)  # Simulate a long-running task
        main()
    print("Script has stopped")

def on_button_click():
    global stop_flag
    stop_flag.clear()  # Reset the flag to allow the task to run
    thread = threading.Thread(target=long_running_task)
    thread.start()

def off_button_click():
    global stop_flag
    stop_flag.set()  # Set the flag to stop the task

class RedirectText(io.StringIO):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)

# Create the main window
root = tk.Tk()
root.title("Control Panel")
root.geometry("500x400")

# Apply a modern style using ttk
style = ttk.Style()
style.theme_use('default')  # 'clam', 'alt', 'default', 'classic' are available themes

# Create a frame for better layout management
frame = ttk.Frame(root, padding="20 20 20 20")
frame.pack(fill='both', expand=True)

# Create the "On" button with green background
on_button = tk.Button(frame, text="On", command=on_button_click, bg="green", fg="white", font=('Helvetica', 12))
on_button.pack(pady=10)

# Create the "Off" button with red background
off_button = tk.Button(frame, text="Off", command=off_button_click, bg="red", fg="white", font=('Helvetica', 12))
off_button.pack(pady=10)

# Create a Text widget to display terminal output
output_text = tk.Text(frame, height=10, wrap='word', font=('Helvetica', 10))
output_text.pack(pady=10, fill='both', expand=True)

# Redirect stdout to the Text widget
sys.stdout = RedirectText(output_text)

# Start the Tkinter event loop
root.mainloop()
