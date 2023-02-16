from tkinter import *
from PIL import ImageTk, Image 


root = Tk()

root.title("sliders")
root.geometry("400x400")
# creating up down sliders
# you 
vertical = Scale(root, from_ = 0, to = 200)
# you can edit this e.g background colour.
# make the pack separate
vertical.pack()

def slide():
	my_label = Label(root, text = horizontal.get()).pack()
	root.geometry(f"{horizontal.get()}x{vertical.get()}")

# with horizontal, you have to change the orient arg
horizontal = Scale(root, from_ = 0, to = 200, orient = HORIZONTAL)
horizontal.pack()


#this will make the button change sliders once clicked
my_btn = Button(root, text = "Click me", command = slide).pack()


root.mainloop()



