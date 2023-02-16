from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("checkboxes")
root.geometry("600x600")


#labels tend to be part of def
def show():
	myLabel = Label(root, text = var.get()).pack()


# you wants boxes to get a 0 or 1 so make in
# you can get boxes to say what they want by changing the type and setting an onvalue and off value.
var = StringVar()
# var.set("0")
# or deselect
c = Checkbutton(root, text = "Please check this box.", variable = var, onvalue = "On", offvalue = "Off" )
c.deselect()
c.pack()



myButton = Button(root, text = "Show Selection", command = show).pack()
root.mainloop()