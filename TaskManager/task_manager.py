import json
import datetime
from utilites import Utilites , Priority , Filter , Sorting
import csv

class TaskManager(Utilites ) :
    def __init__(self):
        self.tasks = []
        self.date_format = "%Y-%m-%d"
        

    # This list will store all taks

    def load_tasks (self) :
        """
        Load tasks from a file when program starts.
        If file does not exist , ignore error.
        """
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []



    def save_tasks (self) :
        """
        Save all tasks to file.
        """
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

    
    

    def add_task (self) :
        """
        Add a new task to the list .
        """

        
        task = input("Enter new task : ")
        
        for x in Priority:
            print(f"{x.value} = {x}")

        user_input = input("Enter task priority (1=LOW, 2=MEDIUM, 3=HIGH): ").strip()
        
        if not self.priority_validation(user_input) :
            return
        
        userinput_date = input("Enter Due date (YYYY-MM-DD) or leave it for automatic : ")

        if userinput_date is "" :
            userinput_date = str(datetime.date.today())
        

        self.tasks.append({
            "id" : self.generate_task_id(),
            "title" : task,
            "completed" : False,
            "priority" : int(user_input),
            "due" : userinput_date,
        })
        self.save_tasks()
        print("Task added successfully!\n")


    def filter (self) :
        """
        Task Filtering by :
        1. Completed
        2. Not Completed
        3. High Priority
        """
        
        for x in Filter :
            print(f"{x.value} = {x}")
        filter_by = int(input("Enter filter number : "))

        if Filter(filter_by).name == Filter.COMPLETED.name :
            for task in self.tasks :
                if task["completed"] :
                    self.print_task(task)
            return
    
        if Filter(filter_by).name == Filter.NOT_COMPLETED.name :
            for task in self.tasks :
                if not task["completed"] :
                    self.print_task(task)
            return
        
        if Filter(filter_by).name == Filter.HIGH_PRIORITY.name :
            for task in self.tasks :
                if task["priority"] ==1 :
                    self.print_task(task)
                
            return
        

        print("Invalid filter number")

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def view_task (self) :
        """
        Display all tasks.
        """
        if not self.tasks :
            print("No task found.\n")
            return
        
        print("\nYour Tasks:")
        # sorted_tasks = sorted(self.tasks, key=lambda x: x["priority"])
        for task in self.tasks :
            self.print_task(task)
           
        print()

    def mark_as_completed (self) :
        """
        Allow users to mark as completed the task.
        """
        self.view_task()
        try :
            number = int(input("Enter the task number to mark as completed : "))
            self.tasks[number-1]["completed"] = True
            self.save_tasks()
            print(f"Task number {number} is successfully marked as complete")
        except(ValueError  , IndexError) :
            print("Invalid task number")

    def delete_task (self) :
        """
        Delete task by number.
        """
        self.view_task()
        try :
            task_id = int(input("Enter task id number to delete : "))
            self.tasks = [task for task in self.tasks if task["id"] != task_id]
            self.save_tasks()
            print(f"Id {task_id} deleted sucessfully \n")
        except (ValueError , IndexError) :
            print("Invalid task number!\n")

    def search_task (self) :
        """
        Search Task by searching title
        """

        searched_text = input("Search : ")
        is_found = 0
        for index  , task in enumerate(self.tasks , start=1) :
            if searched_text.lower() in task["title"].lower() :
                self.print_task(task)
                is_found = True
        
        if not is_found :
            print("Task not found")

    def tasks_statistics(self) :
        """
        This for to show the tasks :
            1. Total tasks: 12
            2. Completed: 5
            3. Pending: 7
            4. Overdue: 3
        """

        if not self.tasks :
            print("No task found.\n")
            return 
        
        total_tasks = len(self.tasks)
        completed = sum(task["completed"] for task in self.tasks)
        pending = sum(not task["completed"] for task in self.tasks)
        overdue = len([task for task in self.tasks if self.string_to_date(task['due']) < self.string_to_date(datetime.date.today().strftime(self.date_format))])

        print(f"1. Total tasks : {total_tasks}")
        print(f"2. Completed : {completed}")
        print(f"3. Pending : {pending}")
        print(f"4. Overdue : {overdue}")
        

    def edit_task(self):

        self.view_task()

        task_id = int(input("Enter task ID to edit: "))

        task = self.get_task_by_id(task_id)

        if not task:
            print("Task not found")
            return

        print("Press Enter to keep current value")

        # TITLE
        title = input(f"New title ({task['title']}): ")
        if title:
            task["title"] = title

        # PRIORITY
        priority = input(f"New priority ({task['priority']}): ")
        if priority:
            if not self.priority_validation(priority):
                return
            task["priority"] = int(priority)

        # DUE DATE
        due = input(f"New due date ({task['due']}): ")
        if due:
            date = self.string_to_date(due)
            if not self.date_validation(date):
                return
            task["due"] = due

        self.save_tasks()
        print("Task updated successfully!")


    def task_sorting(self) :
        """
        This function is used for task sorting by
            1. Priority
            2. Due date
            3. Title
        """

        if not self.tasks :
            print("No task found.\n")
            return
        
        for x in Sorting :
            print(f"{x.value} = {x}")
        sort_by = int(input("Enter Sorting number : "))

        if Sorting(sort_by).name == Sorting.PRIORITY.name :
            self.sort("priority")
            return
    
        if Sorting(sort_by).name == Sorting.DUE_DATE.name :
            self.sort("due")
            return
        
        if Sorting(sort_by).name == Sorting.TITLE.name :
            self.sort("title")
            return

    def export_to_csv (self) :
        if not self.tasks :
            print("No task found.\n")
            return
        
        with open('output.csv', 'w' , newline='') as csvfile :
            fieldnames = ["id" , "title" , "completed" , "priority" , "due"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.tasks)
            print("Successfully exported")

    def print_task(self, task):
        status = "✓" if task["completed"] else "✗"
        
        due_date = self.string_to_date(task['due'])
        today = datetime.datetime.now()

        due_display = "⚠ OVERDUE" if due_date < today and not task["completed"] else task["due"]

        print(
            f"Id. {task["id"]}. [{status}] {task['title']} | "
            f"Priority: {Priority(task['priority']).name} | "
            f"Due: {due_display}"
        )

    def sort (self , sort_by) :
        reverse = input("Do you want reverse (Enter 'y' or 'n') :")
        if reverse.lower() in ("y", "n"):
            task_sorted = sorted(self.tasks, key=lambda x: x[sort_by] , reverse= True if reverse.lower() == 'y' else False)
            
            for task in task_sorted :
                self.print_task(task)
        else :
            print("Invalid input")

    def generate_task_id(self):
        if not self.tasks:
            return 1
        return max(task["id"] for task in self.tasks) + 1
    
    def priority_validation (self , user_input) :
        try:            
            # Check for empty input
            if not user_input:
                print("Priority is required.")
                return False
            else:
                # Check if value exists in enum
                if any(int(user_input) == p.value for p in Priority):
                    return True
                else:
                    print("Invalid priority value.")
                    return False
        except ValueError:
                print("Please enter a valid number.")
                return False
