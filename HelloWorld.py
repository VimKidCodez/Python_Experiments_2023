from tkinter import *

root = Tk()
root.title("Simple Window")

Text = Label(root , text="Hello World")
Text.grid(row=0,column=0)
Button = Button(root,text="Close",command=root.destroy)
Button.grid(row=1,column=0)
root.mainloop()