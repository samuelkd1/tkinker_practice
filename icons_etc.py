
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("icons")
root.iconbitmap("/Users/samkd/Documents/python_lesson/tkinter_practice/Juss_Gym-logos_black.ico")

button_quit = Button(root, text = "Exit Program", command = root.quit)
button_quit.pack()



# using images (hard at first)

my_img = ImageTk.PhotoImage(Image.open("/Users/samkd/Documents/python_lesson/tkinter_practice/Juss_Gym_logos_transparent.png"))

my_label = Label(image = my_img)

my_label.pack()

root.mainloop()
