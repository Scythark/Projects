import tkinter as tk
import calendar
from datetime import date

def show_calendar():
    # Get the current year and month
    current_year = date.today().year
    current_month = date.today().month
    
    # Generate the calendar for the current year and month
    cal_content = calendar.month(current_year, current_month)
    
    # Update the label text with the generated calendar
    label.config(text=cal_content)
    
    # Get the current date
    current_date = date.today().strftime("%B %d, %Y")
    
    # Update the label text to display the current date below the calendar
    date_label.config(text=current_date)

root = tk.Tk()
root.title("Garrett's Calendar Extravaganza!")

button1 = tk.Button(root, text="Month!\n____________________________", command=show_calendar)
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = tk.Button(root, text="Date!:\n____________________________")
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = tk.Button(root, text="Time!:\n____________________________")
button3.grid(row=0, column=2, padx=5, pady=5)

button4 = tk.Button(root, text="Events:\n____________________________")
button4.grid(row=0, column=3, padx=5, pady=5)

# Create a label to display the calendar
label = tk.Label(root, text="")
label.grid(row=1, column=0, padx=5, pady=5, sticky="sw")  # Use sticky="sw" to stick to the bottom-left corner

# Create a label to display the current date
date_label = tk.Label(root, text="", padx=5, pady=5)
date_label.grid(row=2, column=0, padx=5, pady=5, sticky="nw")  # Use sticky="nw" to stick to the top-left corner

root.mainloop()
