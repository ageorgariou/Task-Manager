import datetime

class Task:
    def __init__(self, title, due_date, priority):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.status = "Not Started"

    def update_status(self, status):
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self):
        title = input("Enter task title: ")
        due_date = input("Enter task due date (YYYY-MM-DD): ")
        priority = input("Enter task priority (High, Medium, Low): ")
        task = Task(title, due_date, priority)
        self.tasks.append(task)
        print("Task created successfully!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task.title} - Due: {task.due_date} - Priority: {task.priority} - Status: {task.status}")

    def update_task_status(self):
        if not self.tasks:
            print("No tasks found.")
            return

        self.list_tasks()
        task_index = int(input("Enter the index of the task to update: "))
        if task_index < 1 or task_index > len(self.tasks):
            print("Invalid task index.")
        else:
            task = self.tasks[task_index - 1]
            status = input("Enter the new status (Not Started, In Progress, Completed): ")
            task.update_status(status)
            print("Task status updated successfully!")

    def run(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Create Task")
            print("2. List Tasks")
            print("3. Update Task Status")
            print("4. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.update_task_status()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

task_manager = TaskManager()
task_manager.run()
