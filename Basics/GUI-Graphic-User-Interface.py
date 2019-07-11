# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:52:28 2019

@author: Yusef Quinlan
"""

from tkinter import *
#Create the window
root = Tk()
#Modify the window
root.title("Simple GUI")
root.geometry("200x100")

app = Frame(root)
app.grid()
label = Label(app, text = "this is a label")
label.grid()

#Kick off the app.
root.mainloop()