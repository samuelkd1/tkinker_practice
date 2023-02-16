#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 22:45:57 2023

@author: samkd
"""

from tkinter import *

root = Tk()
# youve made a label
myLabel = Label(root, text = "Hello World!")

# now to put it on the screen by packing

myLabel.pack()

# now to create a event loop

root.mainloop()
