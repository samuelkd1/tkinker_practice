

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("frames this time")

# like with everything with Tk you create and then place wuth grid or pack
frame = LabelFrame(root, padx = 5, pady = 5)
# double padding to make it go in the window
frame.pack(padx = 10, pady = 10)

# now to put things in the frame
# lets create a button

button = Button(frame, text = "dont click here")
button2 = Button(frame, text = "...or here")
button.grid(row = 0, column = 0)
button2.grid(row = 1, column = 0)
root.mainloop()
