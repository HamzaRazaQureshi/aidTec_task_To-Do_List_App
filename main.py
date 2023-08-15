import tkinter as tk
from tkinter import messagebox
import json

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x550")
        self.root.title("TO-DO LIST APP")

        self.tasks = []

        self.title_label = tk.Label(root, text="Title", font=("Arial", 18))
        self.title_label.pack(padx=10, pady=10)

        self.title_entry = tk.Entry(root, width=40, font=('Arial 12'))
        self.title_entry.pack()

        self.description_label = tk.Label(root, text="Description:", font=("Arial", 18))
        self.description_label.pack(padx=10, pady=5)

        self.description_entry = tk.Entry(root, width=40, font=('Arial 12'))
        self.description_entry.pack(pady=5)

        self.tasks_listbox = tk.Listbox(root, width=40, font=('Arial 12'))
        self.tasks_listbox.pack(pady=5)

        self.scrollbar = tk.Scrollbar(root, command=self.tasks_listbox.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.tasks_listbox.config(yscrollcommand=self.scrollbar.set)

        self.add_button = tk.Button(root, bg="lightblue", width=40, font=('Arial 12'), text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, bg="lightblue", width=40, font=('Arial 12'), text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.save_button = tk.Button(root, bg="lightblue", width=40, font=('Arial 12'), text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(root, bg="lightblue", width=40, font=('Arial 12'), text="Load Tasks", command=self.load_tasks)
        self.load_button.pack(pady=5)

        self.update_listbox()

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        if title and description:
            self.tasks.append({"title": title, "description": description})
            self.update_listbox()
        else:
            messagebox.showerror("Error", "Title and description cannot be empty.")

    def delete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_listbox()

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task["title"])

    def save_tasks(self):
        filename = "tasks.json"
        with open(filename, "w") as file:
            json.dump(self.tasks, file)
            messagebox.showinfo("Success", "Tasks saved to tasks.json.")

    def load_tasks(self):
        filename = "tasks.json"
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
                self.update_listbox()
                messagebox.showinfo("Success", "Tasks loaded from tasks.json.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No tasks file found.")

# Driver Code
root = tk.Tk()
app = ToDoListApp(root)
root.update()
root.mainloop()
