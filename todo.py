import sys

TASKS_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: {task}")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("Your To-Do List:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

def remove_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number.")

def show_help():
    print("Usage:")
    print("  python todo.py add \"Task name\"   # Add a new task")
    print("  python todo.py view               # View all tasks")
    print("  python todo.py remove NUMBER      # Remove a task by its number")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
    elif sys.argv[1] == "add" and len(sys.argv) >= 3:
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "view":
        view_tasks()
    elif sys.argv[1] == "remove" and len(sys.argv) == 3:
        try:
            idx = int(sys.argv[2])
            remove_task(idx)
        except ValueError:
            print("Please provide a valid task number.")
    else:
        show_help()