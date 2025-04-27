import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task_index = listbox.curselection()
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def main():
    global entry, listbox

    root = tk.Tk()
    root.title("To-Do List App")
    root.geometry("300x400")
    root.configure(bg="#DFF6FF")

    tk.Label(root, text="Enter Task:", bg="#DFF6FF", font=("Arial", 12)).pack(pady=10)
    
    entry = tk.Entry(root, width=30)
    entry.pack(pady=5)

    tk.Button(root, text="Add Task", width=20, command=add_task).pack(pady=5)
    tk.Button(root, text="Delete Task", width=20, command=delete_task).pack(pady=5)

    listbox = tk.Listbox(root, width=40, height=15)
    listbox.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
