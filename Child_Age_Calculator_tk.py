# Child Age Calculator Written for tkinter
# by Shon Garrison
# Created on: Aug 21, 2025
# Updated on: Aug 2025

import tkinter as tk
from tkinter import ttk
from datetime import date
from ttkbootstrap import Style

window = tk.Tk()
window.geometry("373x299")
window.title("Child Age Calculator")
window.style = Style(theme='darkly')

def calculate_age():
       # get variables
       year_Input = entry_bdyear.get()
       month_Input = entry_bdmonth.get()
       day_Input = entry_bdday.get()
       today = date.today()

       # Convert Varibles to Date
       birthdate = date(year_Input, month_Input, day_Input)

       # Make Calculations
       age_output = int((today - birthdate).days / 365.25)
       
       # If over the age of 18, turn the lable "red"
       if age_output >= 18:
              output_label2.config(foreground="red")
       else:
              output_label2.config(foreground="white")

       output_Results.set(age_output)       


birthdate_label = ttk.Label(master=window, text="Enter Birthdate:", font="Calibri 20 bold")
birthdate_label.pack(anchor='nw', pady=10) 

# Birthday Input Framework ================================================================
input_frame = ttk.Frame(master=window)

entry_bdyear = tk.IntVar()
entry_bdmonth = tk.IntVar()
entry_bdday = tk.IntVar()

entry1 = ttk.Entry(master=input_frame, width=4, textvariable=entry_bdmonth, font="Calibri 16")
entry1.pack(side=tk.LEFT, padx=10)

label1 = ttk.Label(master=input_frame, text="/", font="Calibri 16")
label1.pack(side=tk.LEFT)

entry2 = ttk.Entry(master=input_frame, width=4, textvariable=entry_bdday, font="Calibri 16")
entry2.pack(side=tk.LEFT, padx=10)


label2 = ttk.Label(master=input_frame, text="/", font="Calibri 16")
label2.pack(side=tk.LEFT)

entry3 = ttk.Entry(master=input_frame, width=4, textvariable=entry_bdyear, font="Calibri 16")
entry3.pack(side=tk.LEFT, padx=10)

input_frame.pack(anchor='nw', pady=10)
 
# Output Framework ========================================================================
output_Frame = ttk.Frame(master=window)

output_Results = tk.IntVar()

output_label = ttk.Label(master=output_Frame, text="Child's Age: ", font="Calibri 14")
output_label.pack(side=tk.LEFT, pady=40)

output_label2 = ttk.Label(master=output_Frame, 
                          font="Calibri 15", 
                          textvariable=output_Results, 
                          foreground="White"
                          )
output_label2.pack(side=tk.LEFT, padx=10)

output_label3 = ttk.Label(master=output_Frame, text = "Years Old", font="Calibri 14")
output_label3.pack(side=tk.LEFT, padx=10)

output_Frame.pack(anchor = 'w', pady=10)

# Button Framework =========================================================================
button_frame = ttk.Frame(master=window)

button1 = ttk.Button(master=button_frame, width=9, text="Calculate", command=calculate_age)
button1.pack(side=tk.LEFT, padx=10)

button2 = ttk.Button(master=button_frame, width=9, 
                     text="Clear", 
                     command=lambda: (output_label2.config(foreground="white"), 
                                      entry_bdday.set(0), 
                                      entry_bdmonth.set(0), 
                                      entry_bdyear.set(0), 
                                      output_Results.set(0))
                     )
button2.pack(side=tk.LEFT, padx=10)

button3 = ttk.Button(master=button_frame, width=9, text="Close", command=window.destroy)
button3.pack(side=tk.LEFT, padx=10)

button_frame.pack(anchor = 's', pady=10)



# Run Applications ========================================================================
window.mainloop()
print("\nGood-Bye\nApplication Terminated")