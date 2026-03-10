from tkinter import *

root = Tk()
root.title("Visual studio Code")
root.geometry("800x500")
root.minsize(400 , 200)
root.config(background="#38003d")

# Top Header
header = Frame(root , background="#680471" , padx=2)
navList1 = Label(header, text="File"  , font=("Nunito Sans" , 12),  background="#680471", fg="white"  , padx=10)
navList2 = Label(header, text="Edit" , font=("Nunito Sans" , 12) ,   background="#680471", fg="white" , padx=10)
navList3 = Label(header, text="Selection" , font=("Nunito Sans" , 12), background="#680471", fg="white" , padx=10)
navList4 = Label(header, text="View" , font=("Nunito Sans" , 12), background="#680471", fg="white" , padx=10)
navList5 = Label(header, text="Go" , font=("Nunito Sans" , 12),  background="#680471",fg="white" , padx=10)
navList6 = Label(header, text="Run" , font=("Nunito Sans" , 12), background="#680471", fg="white" , padx=10)

# Side bar

sidebar = Frame(root , background="#680471" , pady=20 , padx=30)
file1Frame = Frame(sidebar , background="#680471")
file1 = Label(file1Frame , background="#680471" , text="project.py" , fg="white" ,font=("Nunito Sans" , 12))

header.pack(side=TOP , fill="x" )
navList1.pack(side=LEFT)
navList2.pack(side=LEFT)
navList3.pack(side=LEFT)
navList4.pack(side=LEFT)
navList5.pack(side=LEFT)
navList6.pack(side=LEFT)
sidebar.pack(side=LEFT, fill="y")
file1.pack()
file1Frame.pack(side=TOP)
file1.pack(side=LEFT)


root.mainloop()
