from tkinter import *

root = Tk()

root.geometry("370x400")
photo = PhotoImage(file="image.png")

lable = Label(image=photo)
lable.pack()

root.mainloop()
