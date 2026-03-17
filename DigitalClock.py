from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.configure(bg="black")

clock_lable = Label(
    root,
    font=("calibri" , 50 , "bold"),
    background="black",
    foreground="cyan"
)

clock_lable.pack(anchor="center" , expand=True)


def update_time () :
    current_time = strftime("%H:%M:%S %p")
    clock_lable.config(text=current_time)
    clock_lable.after(1000 , update_time)


update_time()

root.mainloop()
