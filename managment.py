class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task.completed else "Pending"
                print(f"{index}. Title: {task.title}, Status: {status}, Due Date: {task.due_date}")

    def update_task(self, index, title, description, due_date):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.title = title
            task.description = description
            task.due_date = due_date
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            deleted_task = self.tasks.pop(index)
            print(f"Deleted task: {deleted_task.title}")
        else:
            print("Invalid task index.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (yyyy-mm-dd): ")
            task = Task(title, description, due_date)
            task_manager.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            index = int(input("Enter the index of the task to update: "))
            title = input("Enter new task title: ")
            description = input("Enter new task description: ")
            due_date = input("Enter new due date (yyyy-mm-dd): ")
            task_manager.update_task(index, title, description, due_date)
        elif choice == "4":
            index = int(input("Enter the index of the task to mark as completed: "))
            task_manager.complete_task(index)
        elif choice == "5":
            index = int(input("Enter the index of the task to delete: "))
            task_manager.delete_task(index)
        elif choice == "6":
            print("Exiting the Task Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
