class Task:
    """
    A class to represent a Task.
    """

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}"


class TaskManager:
    """
    A class to manage a list of tasks with CRUD operations.
    """

    def __init__(self):
        self.tasks = []

    def create_task(self, title: str, description: str):
        task = Task(title, description)
        self.tasks.append(task)
        print("✅ Task created successfully!\n")

    def read_tasks(self):
        if not self.tasks:
            print("⚠️ No tasks available.\n")
            return

        print("\n📋 List of Tasks:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"\nTask {idx}:\n{task}")

    def update_task(self, index: int, new_title: str, new_description: str):
        if 0 <= index < len(self.tasks):
            self.tasks[index].title = new_title
            self.tasks[index].description = new_description
            print("✅ Task updated successfully!\n")
        else:
            print("❌ Invalid task number.\n")

    def delete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("🗑️ Task deleted successfully!\n")
        else:
            print("❌ Invalid task number.\n")


def main():
    manager = TaskManager()

    while True:
        print("\n===== Task Manager =====")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.create_task(title, description)

        elif choice == "2":
            manager.read_tasks()

        elif choice == "3":
            manager.read_tasks()
            try:
                index = int(input("Enter task number to update: ")) - 1
                new_title = input("Enter new title: ")
                new_description = input("Enter new description: ")
                manager.update_task(index, new_title, new_description)
            except ValueError:
                print("❌ Please enter a valid number.\n")

        elif choice == "4":
            manager.read_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                manager.delete_task(index)
            except ValueError:
                print("❌ Please enter a valid number.\n")

        elif choice == "5":
            print("👋 Exiting the Task Manager. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select between 1 and 5.\n")


if __name__ == "__main__":
    main()
