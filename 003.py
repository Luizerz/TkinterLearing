import tkinter as tk
from tkinter import ttk


# Functions
def buttonFunc():
    # get the content of entry
    print(entry.get())
    
    #update the label
    label.config(text = entry.get())
    entry.config(state = 'disable')

def resetFunc(): 
    label.config(text = 'Label')
    entry.config(state = 'enable')

# window
window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry('500x500')

# widgets
label = ttk.Label(
    master = window, 
    text = 'Label'
    )
entry = ttk.Entry(master = window)
button = ttk.Button(
    master = window, 
    text = 'Atualizar label',
    command = buttonFunc
    )
button2 = ttk.Button(
    master = window,
    text = "Reset",
    command = resetFunc
)


# packing
label.pack()
entry.pack()
button.pack()
button2.pack()

# run
window.mainloop()