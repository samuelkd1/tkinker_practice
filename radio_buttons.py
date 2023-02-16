
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("radio button")

# we have to define variables for tkinter has to be an integer because the values are integers

##r = IntVar()
# we need to grab the variable too
##r.get()
##r.set("1")
# lets say pizza toppings

MODES = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),

    ]

pizza = StringVar()

pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text = text, variable = pizza, value = mode).pack(anchor = W)

def clicked(value):
    myLabel = Label(root, text = value)
    myLabel.pack()

                    
#Radiobutton(root, text = "Option 1", variable = r, value = 1, command = lambda: clicked(r.get())).pack()
#Radiobutton(root, text = "Option 2", variable = r, value = 2, command = lambda: clicked(r.get())).pack()

#myLabel = Label(root, text = pizza.get())
#myLabel.pack()

myButton = Button(root, text = "click me!", command = lambda: clicked(pizza.get()))

myButton.pack()


root.mainloop()
