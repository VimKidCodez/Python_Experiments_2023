from tkinter import *

root = Tk()

root.title("chnage my color button")


def click_me():
	Button_1["fg"] = "blue"


Button_1 = Button(root,text="Click me",command=click_me)
Button_1.grid(row=1,column=2)
root.mainloop()