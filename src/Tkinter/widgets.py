'''
Created on 13 kwi 2018

@author: Roju
'''
from tkinter import *
from tkinter import ttk

root = Tk()

button = ttk.Button(root,text="Click me!")
button.pack()

button['text'] = 'Press me' #first method of change text on button
button.config(text='Push me') # second method of change text on button

ttk.Label(root, text = 'Hello, Tkinter !').pack()

root.mainloop()
