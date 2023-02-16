
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("creating_new_windows")
root.iconbitmap("Juss_Gym_logos_black.ico")
# this will divide your windows into different levels

# below is for controlling when window(s) pop up

def open():
    # you gotta call global so it can be registered elsewehere.
    global my_image
    top = Toplevel()
    top.title("window_2")
    top.iconbitmap("Juss_Gym_logos_black.ico")
    my_image = ImageTk.PhotoImage(Image.open("images/Juss_Gym_logos_black.png"))
    my_Label = Label(top, image = my_image).pack()

    # .destrow will exit

    button2 = Button(top, text = "close window", command = top.destroy).pack()
    

button = Button(root, text = "Open Second Window", command = open).pack()





root.mainloop()
