#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 22:45:57 2023

@author: samkd
"""

from tkinter import *

root = Tk()

e = Entry(root, width = 50, borderwidth = 5)
e.pack()

# to get the button to do something, we need to define a function

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root,text = hello)
    myLabel.pack()
    
# this is how you make a button # state disabled will grey things out
myButton = Button(root, text = "Enter Your Name", command = myClick, fg = "red", padx = 50, pady = 25)
myButton.pack()

root.mainloop()
