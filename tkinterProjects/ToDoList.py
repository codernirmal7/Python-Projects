from tkinter import *
import json

class ToDOListApp () :
    def __init__(self , root , file_path):
        self.root = root
        self.root.title("To DO List")
        self.root.geometry("500x300")
        self.root.minsize(400 , 200)
        self.root.configure(bg="#e8f0f8")
        self.file_path = file_path
        self.setup_ui()


    def setup_ui (self) :
        self.topic_value = StringVar()
        self.description_value = StringVar()
        
        self.topic = Label(self.root ,  text="Topic")
        self.description = Label(self.root , text="Description")

        self.topic_entry = Entry(self.root , textvariable=self.topic_value)
        self.description_entry = Entry(self.root , textvariable=self.description_value)


        self.submit_btn = Button(text="Add" , pady=4 , padx=50 , background="red" , command=lambda : self.add_data(self.load_data()))

        self.todo_list = Label(text=self.load_data())

        self.topic.grid()
        self.description.grid()
        self.topic_entry.grid(row=0 , column=1)
        self.description_entry.grid(row=1 , column=1)
        self.submit_btn.grid(pady=10)
        self.todo_list.grid(row=3 )

    def update_ui (self) :
        self.todo_list.config(text=self.load_data())
    
    def load_data (self) :
        try :
            with open(self.file_path) as file :
                return json.load(file)
        except FileNotFoundError :
            return []
        
    

        
    def list_all_data (self , list_data) :
        list_array_data = []
        for index , data in enumerate(list_data , start=1) :
            list_array_data.append({data})
            print(data)
        return list_array_data
    
    def save_data_helper (self , data) :
        with open(self.file_path , "w") as file :
            json.dump(data , file)

    def add_data (self , data) :
        data.append({
            "topic" : self.topic_value.get(),
            "description" : self.description_value.get()
        })
        self.save_data_helper(data)
        self.update_ui()
        
        



if __name__ == "__main__" :
    root = Tk()
    app = ToDOListApp(root , "todolist.txt")    
    root.mainloop()
