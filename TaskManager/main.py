from task_manager import TaskManager

def main () :
    task_manager = TaskManager()

    task_manager.load_tasks()

    while True :
        print("1. Add Task")
        print("2. View Task")
        print("3. Delete Task")
        print("4. Mark as complete to Task")
        print("5. Search Task")
        print("6. Edit task")
        print("7. Filter task")
        print("8. Task statistics")
        print("9. Task Sorting")
        print("10. Export task into csv file")
        print("11. Exit")

        choice = input("Choose option : ")

        if choice == "1" :
            task_manager.add_task()
        elif choice == "2" :
            task_manager.view_task()
        elif choice == "3" :
            task_manager.delete_task()
        elif choice == "4" :
            task_manager.mark_as_completed()
        elif choice == "5" :
            task_manager.search_task();
        elif choice == "6" :
            task_manager.edit_task();
        elif choice == "7" :
            task_manager.filter()
        elif choice == "8" :
            task_manager.tasks_statistics()
        elif choice == "9" :
            task_manager.task_sorting()
        elif choice == "10" :
            task_manager.export_to_csv()
        elif choice == "11" :
            break
        else :
            print("Invalid choice!\n")

if __name__ == "__main__" :
    main()
