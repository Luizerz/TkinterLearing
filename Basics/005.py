import tkinter as tk
from tkinter import ttk

# functions
def checkFunc():
    print(checkVar.get())

# window
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

# tkVariables
checkVar = tk.BooleanVar(value = True)

# widgets
button = ttk.Button(
    window,
    text = 'A Simple button',
    )

check = ttk.Checkbutton(
    window,
    text = 'checkbox 1',
    command = checkFunc,
    variable = checkVar
    )

radial = ttk.Radiobutton(
    window,
    text = 'RadialButton'
    )

# packing
button.pack()
check.pack()
radial.pack()

# run
window.mainloop()