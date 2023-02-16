from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("drop down box")
root.geometry("600x600")

def show():
	myLabel = Label(root, text = clicked.get()).pack()

options = ["Mon","Tues","Weds","Thurs","Fri"]

# define var

clicked = StringVar()

clicked.set(options[0])
#below are the func and args
dropdown = OptionMenu(root, clicked, *options)
dropdown.pack()


myButton = Button(root, text = "Show Selection", command = show)
myButton.pack()

root.mainloop()