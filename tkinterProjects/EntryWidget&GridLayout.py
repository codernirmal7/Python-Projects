from tkinter import *

def getFormValue () :
    print(f"Saved Email : {emailValue.get()}")
    print(f"Saved Password : {passValue.get()}")


root = Tk()
root.geometry("500x300")



emailLable = Label(root , text="Email")
passLable = Label(root , text="Password")
emailLable.grid(row=0) # you don't need to write "row=0" because it's default value
passLable.grid(row=1)

emailValue = StringVar()
passValue = StringVar()

emailInput = Entry(root , textvariable=emailValue)
passInput = Entry(root , textvariable=passValue)
emailInput.grid(row=0 , column=1)
passInput.grid(row=1 , column=1)

Button(text="Submit" , command=getFormValue).grid(column=1)

root.mainloop()
