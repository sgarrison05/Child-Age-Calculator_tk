# Child Age Calculator Written for tkinter
# by Shon Garrison
# Created on: Aug 21, 2025
# Updated on: Sept 2025

import tkinter as tk
from tkinter import ttk
from datetime import date
from tkcalendar import DateEntry

window = tk.Tk()
window.geometry("400x300")
window.title("Child Age Calculator")
#window.style = Style(theme='darkly')

def calculate_age():
       # get variables
       bd = cal.get_date()      
       today = date.today()

       # Make Calculations
       age_output = int((today - bd).days / 365.25)
       
       # If over the age of 18, turn the lable "red"
       if age_output >= 18:
              output_label2.config(foreground="red")
       else:
              output_label2.config(foreground="black")

       output_Results.set(age_output)


birthdate_label = ttk.Label(window, text="Enter Birthdate:", font="Calibri 20 bold")
birthdate_label.pack(anchor='nw', pady=10) 

# Birthday Input Framework ================================================================

cal = DateEntry(window, date_pattern="mm/dd/yyyy", font='Calibri, 12')
cal.place(x=10,y=50, height=26)
 
# Output Framework ========================================================================
output_Frame = ttk.Frame(window)

output_Results = tk.IntVar()

output_label = ttk.Label(output_Frame, text="Child's Age: ", font="Calibri 14")
output_label.pack(side=tk.LEFT, pady=40)

output_label2 = ttk.Label(output_Frame, font="Calibri 15", textvariable=output_Results)
output_label2.pack(side=tk.LEFT, padx=10)

output_label3 = ttk.Label(output_Frame, text = "Years Old", font="Calibri 14")
output_label3.pack(side=tk.LEFT, padx=10)

output_Frame.pack(anchor = 'w', padx=10, pady=25)

# Button Framework =========================================================================
button_frame = ttk.Frame(window)

button1 = ttk.Button(button_frame, width=9, text="Calculate", command=calculate_age)
button1.pack(side=tk.LEFT, padx=10)

button2 = ttk.Button(button_frame, width=9, text="Clear", command=lambda: (output_Results.set(0), cal.set_date(date.today())))                     
button2.pack(side=tk.LEFT, padx=10)

button3 = ttk.Button(button_frame, width=9, text="Close", command=window.destroy)
button3.pack(side=tk.LEFT, padx=10)

button_frame.pack(anchor = 's', padx=10, pady=10)


# Run Applications ========================================================================
window.mainloop()
print("\nGood-Bye\nApplication Terminated")