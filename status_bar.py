
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("icons")
root.iconbitmap("Juss_Gym_logos_black.ico")


# using images (hard at first)

my_img1 = ImageTk.PhotoImage(Image.open("images/Juss_Gym_logos_black.png"))

my_img2 = ImageTk.PhotoImage(Image.open("images/Juss_Gym_logos_transparent_30.png"))

my_img3 = ImageTk.PhotoImage(Image.open("images/Juss_Gym_logos_white.png"))

my_img4 = ImageTk.PhotoImage(Image.open("images/Juss_Gym_logos.jpeg"))

my_img5 = ImageTk.PhotoImage(Image.open("images/Juss_munch_logos_black.png"))

my_img6 = ImageTk.PhotoImage(Image.open("images/Juss_munch_logos_transparent.png"))

# you gotta make a list of all the images

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)


my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)

# we need functions now
def forward(imageno):

    global mylabel
    global button_forward
    global button_back
    
    my_label.grid_forget()
    
    mylabel = Label(image = image_list[imageno - 1])
    button_forward = Button(root, text = ">>", command = lambda: forward(imageno + 1))
    button_back = Button(root, text = "<<", command = lambda: back(imageno - 1))

    if imageno == 6:
        button_forward = Button(root, text = ">>", state = DISABLED)

    status = Label(root, text = f"Image {imageno} of {len(image_list)}" , bd = 1, relief = SUNKEN, anchor = W)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)
  
    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)
    
def back(imageno):
    global mylabel
    global button_forward
    global button_back

    my_label.grid_forget()
    #these will stay the same 
    mylabel = Label(image = image_list[imageno - 1])
    button_forward = Button(root, text = ">>", command = lambda: forward(imageno + 1))
    button_back = Button(root, text = "<<", command = lambda: back(imageno - 1))

    if imageno == 1:
        button_back = Button(root, text = "<<", state = DISABLED) 



    mylabel.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)

    status = Label(root, text = f"Image {imageno} of {len(image_list)}" , bd = 1, relief = SUNKEN, anchor = W)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)
   
    


#the actual commnds
button_back = Button(root, text = "<<", command = back)
button_exit = Button(root, text = "EXIT PROGRAM", command = root.quit)
button_forward = Button(root, text = ">>", command = lambda: forward(2))

# placements
button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2, pady = 10)
status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)

root.mainloop()
