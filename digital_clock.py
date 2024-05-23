import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Set the window size
root.geometry("300x150")

# Configure the label to display the time
time_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
time_label.pack(expand=True)

def update_time():
    # Get the current time and format it
    current_time = time.strftime("%H:%M:%S")
    # Update the label with the current time
    time_label.config(text=current_time)
    # Call this function again after 1000ms (1s)
    root.after(1000, update_time)

# Initial call to update_time to start the clock
update_time()

# Run the main event loop
root.mainloop()
