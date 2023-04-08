import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Tkinter variables')
window.geometry('300x300')

# tkinter variable 
stringVar = tk.StringVar()

# widgets
label = ttk.Label(
    master = window, 
    text = 'CustomLabel',
    textvariable = stringVar
    )
entry = ttk.Entry(
    master = window,
    textvariable = stringVar
    )

# packing
label.pack()
entry.pack()

#run
window.mainloop()