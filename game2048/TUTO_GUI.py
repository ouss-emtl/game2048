from tkinter import *

# Window creation, root of the interface
window = Tk()

# Creation of a label (text line) that says Hello World ! and with as first parameter the previous window
label_field = Label(window,text="Hello World !")

# Display of the label
label_field.pack()

# Running of the Tkinter loop that ends when we close the windw
window.mainloop()

import tkinter as tk


def write_text():
    print("Hello CentraleSupelec")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   activebackground = "blue",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   fg="blue",
                   text="Hello",
                   command=write_text)
slogan.pack(side=tk.LEFT)

root.mainloop()

from tkinter import Tk, StringVar, Label, Entry, Button
from functools import partial

def update_label(label, stringvar):
    """
    Met à jour le texte d'un label en utilisant une StringVar.
    """
    text = stringvar.get()
    label.config(text=text)
    stringvar.set('merci')

root = Tk()
text = StringVar(root)
label = Label(root, text='Your name')
entry_name = Entry(root, textvariable=text)
button = Button(root, text='clic',
                command=partial(update_label, label, text))

label.grid(column=0, row=0)
entry_name.grid(column=0, row=1)
button.grid(column=0, row=2)

root.mainloop()

from tkinter import Tk, Label, Frame

root = Tk()
f1 = Frame(root, bd=1, relief='solid')
Label(f1, text='je suis dans F1').grid(row=0, column=0)
Label(f1, text='moi aussi dans F1').grid(row=0, column=1)

f1.grid(row=0, column=0)
Label(root, text='je suis dans root').grid(row=1, column=0)
Label(root, text='moi aussi dans root').grid(row=2, column=0)

root.mainloop()
