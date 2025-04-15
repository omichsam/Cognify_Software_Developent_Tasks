#  Task Manager Console App (with File I/O)

A simple Python console application for managing a list of tasks using **basic CRUD operations** (Create, Read, Update, Delete) and **persistent storage** using a text file.

---

##  Objective

- Implement a task management app with:
  - Task creation, viewing, editing, and deletion
  - Persistent storage using file I/O
  - Error handling for file operations

---

##  Features

-  Add new tasks
-  View existing tasks
-  Update task details
-  Delete tasks
-  Save and load tasks from a text file (`tasks.txt`)
-  Handles invalid inputs and file errors

---

##  File Structure

task-manager/ 

├── task_manager.py  <i># Main console app </i>

├── tasks.txt    <i># Text file storing task data </i>(auto-created) 

├── README.md  <i># Project documentation</i>


---

##  How to Run the App

### 1. Clone or Download the Repository

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```
### 2. Run the App 
```
python task_manager.py
💡 Use python3 if you're on macOS/Linux
```
### Sample Usage 

```
===== Task Manager =====
1. Create Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit

Enter your choice (1-5): 1

Enter task title: Buy groceries

Enter task description: Milk, Eggs, Bread

- Task created successfully.
- Persistent Storage
- All tasks are stored in a plain text file named tasks.txt

Each task is saved as: title|description

Tasks are automatically loaded at startup and saved after any change
```

## Error Handling
- Handles missing or corrupted file gracefully

- Provides user-friendly error messages for invalid inputs (like letters where numbers are expected)

###  Author
Your Name : Samson Michira

GitHub: <a href="https://github.com/omichsam"><b>omichsam</b></a>

### Contributions
Pull requests and suggestions are welcome. Please open an issue first to discuss your ideas or fixes.


---

Let me know if you'd like a GUI version of this app or a JSON/CSV version for structured task storage!
