#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 22:45:57 2023

@author: samkd
"""

from tkinter import *

root = Tk()
# youve made a label
myLabel1 = Label(root, text = "Hello World!")
myLabel2 = Label(root, text = "My name is KD")
# label as whitespace to separate
#myLabel3 = Label(root, text = " ")

# Grid system

myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 5)
# label as whitespace to separate this will be the positining
#myLabel3.grid(row = 1, column = 1)
# now to create a event loop

root.mainloop()
