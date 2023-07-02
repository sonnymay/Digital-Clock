import time
import tkinter as tk
from tkinter import ttk

def update_time():
    # Get the current time in the format Hour:Minute:Second
    current_time = time.strftime("%H:%M:%S")
    # Update the time_label with the current time
    time_label.config(text=current_time)
    # Call the update_time function again after 1 second
    root.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Set the font and size for the clock
font = ("Helvetica", 48)

# Create a label to display the time
time_label = ttk.Label(root, font=font)
time_label.pack(expand=True)

# Call the update_time function to update the time initially
update_time()

# Run the main loop
root.mainloop()
