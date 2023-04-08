import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

### MILES TO KM CONVERTER
# functions

def convert(): 
    mileInput = entryInt.get()
    kmOutput = mileInput * 1.61
    outputString.set(kmOutput)

# window
window = ttk.Window(themename = 'darkly')
window.title('Km Converter')
window.geometry('350x180')

# title - wideget - 
titleLabel = ttk.Label(master = window, text = 'Miles to Kilometer', font = 'Calibri 24 bold')
titleLabel.pack()

# input field - widget -
inputFrame = ttk.Frame(master = window)
entryInt = tk.IntVar()
entry = ttk.Entry(master = inputFrame, textvariable = entryInt)
button = ttk.Button(master = inputFrame, text = "Convert", command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
inputFrame.pack(pady = 10)

# output - widget -
outputString = tk.StringVar()
outputLabel = ttk.Label(master = window, textvariable = outputString, font = 'Calibri 24')
outputLabel.pack(pady = 5)

# run
window.mainloop()