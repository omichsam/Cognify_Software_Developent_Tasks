import os

TASKS_FILE = "tasks.txt"


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        return f"{self.title}|{self.description}"

    @staticmethod
    def from_string(task_str):
        parts = task_str.strip().split("|")
        if len(parts) == 2:
            return Task(parts[0], parts[1])
        return None


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Loads tasks from the file into memory."""
        if not os.path.exists(TASKS_FILE):
            return
        try:
            with open(TASKS_FILE, "r") as file:
                for line in file:
                    task = Task.from_string(line)
                    if task:
                        self.tasks.append(task)
        except Exception as e:
            print(f"❌ Error loading tasks: {e}")

    def save_tasks(self):
        """Saves current tasks to the file."""
        try:
            with open(TASKS_FILE, "w") as file:
                for task in self.tasks:
                    file.write(str(task) + "\n")
        except Exception as e:
            print(f"❌ Error saving tasks: {e}")

    def create_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        task = Task(title, description)
        self.tasks.append(task)
        self.save_tasks()
        print("✅ Task created successfully.")

    def read_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\n📋 Task List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task.title} - {task.description}")

    def update_task(self):
        self.read_tasks()
        if not self.tasks:
            return
        try:
            index = int(input("Enter task number to update: ")) - 1
            if 0 <= index < len(self.tasks):
                title = input("Enter new title: ")
                description = input("Enter new description: ")
                self.tasks[index].title = title
                self.tasks[index].description = description
                self.save_tasks()
                print("✅ Task updated successfully.")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")

    def delete_task(self):
        self.read_tasks()
        if not self.tasks:
            return
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(self.tasks):
                deleted = self.tasks.pop(index)
                self.save_tasks()
                print(f"🗑️ Task '{deleted.title}' deleted.")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")


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
            manager.create_task()
        elif choice == "2":
            manager.read_tasks()
        elif choice == "3":
            manager.update_task()
        elif choice == "4":
            manager.delete_task()
        elif choice == "5":
            print("👋 Exiting Task Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
