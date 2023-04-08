import tkinter as tk
from tkinter import ttk


# functions 
def buttonFunc(): 
    print('The button was pressed')


# create a window
# nomes alternaviso para window: root ou app
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')


# ttk widgets
label = ttk.Label(
    master = window,
    text = 'This is a ttktest'
    )
label.pack()

# create widgets
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack(pady = 10)

# ttk button
button = ttk.Button(
    master = window, 
    text = 'A Button',
    command = buttonFunc
    )
button.pack()

# run
window.mainloop()