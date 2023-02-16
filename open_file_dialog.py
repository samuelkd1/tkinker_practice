from tkinter import *
from PIL import ImageTk, Image 
# you need to import opening file stuff separately
from tkinter import filedialog

root = Tk()
root.title("opening files")
root.iconbitmap("Juss_Gym_logos_black.ico")

# this will return the name of the file only, once you have the location, you can open the file.
# title will be title of popup box 
# filetypes arg will filter what filetypes you want 
# you separate filetypes by a comma


def open():
	global myImage
	# will open image in window once the image is clicked 
	root.filename = filedialog.askopenfilename(initialdir = "tkinter_practice/images", title = "Select a File", filetypes = (("png files","*.png"),("all_files", "*.*" )))
	myLabel = Label(root, text = root.filename).pack()
	myImage = ImageTk.PhotoImage(Image.open(root.filename))
	my_image_label = Label(image = myImage).pack()

# will open as a button
my_btn = Button(root, text = "Open", command = open).pack()




root.mainloop()