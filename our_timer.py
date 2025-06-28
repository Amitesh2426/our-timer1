import tkinter as tk
from datetime import datetime
from tkinter import messagebox

# Set the starting time
start_time = datetime(2025, 1, 26, 22, 52)

def update_timer():
    now = datetime.now()
    elapsed = now - start_time
    total_seconds = int(elapsed.total_seconds())

    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Format the time string
    time_str = f"{hours}h:{minutes:02}m:{seconds:02}s"
    label.config(text=f"Time since 26 Jan 2025, 10:52 PM:\n{time_str}")

    root.after(1000, update_timer)

def love_clicked():
    messagebox.showinfo("❤️ Love", "Don’t worry dear,\nthis clock will go on forever 💖")
    fade_in_message("💖I Love You Maa💖")

def fade_in_message(text):
    heart_label.config(text=text)
    heart_label.place(relx=0.5, rely=0.8, anchor="center")
    fade_in(0)

def fade_in(step):
    # Simulate fade-in using gradually increasing color brightness
    colors = ["#330033", "#660066", "#990099", "#CC00CC", "#FF33FF"]
    if step < len(colors):
        heart_label.config(fg=colors[step])
        root.after(150, lambda: fade_in(step + 1))

# Create the GUI window
root = tk.Tk()
root.title("Time Elapsed Since 26 Jan 2025, 10:52 PM")
root.geometry("750x250")
root.resizable(False, False)

# Main timer label
label = tk.Label(root, text="", font=("Helvetica", 18, "bold"), justify="center")
label.pack(pady=10)

# Love button
love_button = tk.Button(root, text="❤️Click to stop", font=("Helvetica", 14), command=love_clicked)
love_button.pack(pady=5)

# Heart message label (initially empty and hidden)
heart_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), justify="center")
heart_label.place_forget()

# Start the timer update loop
update_timer()

# Run the app
root.mainloop()
