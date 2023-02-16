
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("message_box")

# different types of message boxes below
# showinfo, showwarning(rtns ok), askquestion, askokcancel(rtns yes no),askyesno(rtns 1, 0), showerror (rtns ok)

def popup():
    # make into variable
    response = messagebox.askyesno("This is my Popup!", "Hello World")
    Label(root, text = response).pack()
    #if response == 1:
    #    Label(root, text = "You clicked yes").pack()
    #else:
    #    Label(root, text = "You clicked no").pack()
        

Button(root, text = "Popup", command = popup).pack()

root.mainloop()
