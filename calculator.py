#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 22:45:57 2023

@author: samkd
"""

from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

#e.insert(0, "Enter your Name: ")
# to get the button to do something, we need to define a function
#create buttons

#lets pass a param we can call em normally
def button_click(number):
   # e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)

# we need this to remember the thing previously so we can add, use of global variables

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplcation":
        e.insert(0, f_num * int(second_number))
        
    if math == "division":
        e.insert(0, f_num / int(second_number))

    if math == "exponent":
         e.insert(0, f_num ** int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)



def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

  
def button_divide():
    
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_exp():
    first_number = e.get()
    global f_num
    global math
    math = "exponent"
    f_num = int(first_number)
    e.delete(0, END)
  
    
# define buttons


# my for loop attempt (almost worked)
#for i in list(range(0,3)):
    #button_i = Button(root, text = str(i+7), padx = 40, pady = 20, command = lambda: button_click(i+7))
    #button_i.grid(row = 3, column = 0+i)
   
#for i in list(range(0,3)):
    #button_i = Button(root, text = str(i+4), padx = 40, pady = 20, command = lambda: button_click(i+4))
    #button_i.grid(row = 2, column = 0+i)

#for i in list(range(0,3)):
    #button_i = Button(root, text = str(i+1), padx = 40, pady = 20, command = lambda: button_click(i+1))
    #button_i.grid(row = 1, column = 0+i)

#button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
#button_0.grid(row = 4 , column = 0)

#button_clear = Button(root, text = "clear", padx = 79, pady = 20, command = button_clear)
#button_clear.grid(row = 5, column = 1, columnspan = 2)

button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
button_add = Button(root, text = "+", padx = 39, pady = 20, command = button_add)

button_equal = Button(root, text = "=", padx = 93, pady = 20, command = button_equal)
button_clear = Button(root, text = "clear", padx = 79, pady = 20, command = button_clear)
button_subtract = Button(root, text = "-", padx = 39, pady = 20, command = button_subtract)
button_multiply = Button(root, text = "*", padx = 39, pady = 20, command = button_multiply)
button_divide = Button(root, text = "/", padx = 39, pady = 20, command = button_divide)
button_exp = Button(root, text = "exp", padx = 39, pady = 20, command = button_exp)


#put buttons on screen
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4 , column = 0)
button_add.grid(row = 4, column = 1)
button_equal.grid(row = 4, column =2, columnspan = 2) 
button_clear.grid(row = 5, column = 2, columnspan = 2)

button_subtract.grid(row = 5 , column = 0)
button_multiply.grid(row = 5 , column = 1)
button_divide.grid(row = 6, column = 0)
button_exp.grid(row = 6, column = 1)



# this is how you make a button # state disabled will grey things out
myButton = Button(root, text = "Enter Your Name", command = button_add, fg = "red", padx = 50, pady = 25)


root.mainloop()
