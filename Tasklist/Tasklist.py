import tkinter as tk
from tkinter import messagebox

class TaskListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Task List")

        # Main frame
        frame = tk.Frame(master, padx=10, pady=10)
        frame.pack(fill="both", expand=True)

        # Entry + Add button
        entry_frame = tk.Frame(frame)
        entry_frame.pack(fill="x", pady=(0, 10))

        self.task_entry = tk.Entry(entry_frame)
        self.task_entry.pack(side="left", fill="x", expand=True)
        self.task_entry.bind("<Return>", self.add_task_event)

        add_button = tk.Button(entry_frame, text="Add", width=10, command=self.add_task)
        add_button.pack(side="left", padx=(5, 0))

        # Listbox + scrollbar
        list_frame = tk.Frame(frame)
        list_frame.pack(fill="both", expand=True)

        self.tasks_listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE)
        self.tasks_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.tasks_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tasks_listbox.yview)

        # Buttons for operations
        button_frame = tk.Frame(frame)
        button_frame.pack(fill="x", pady=(10, 0))

        done_button = tk.Button(button_frame, text="Mark as Done", command=self.mark_done)
        done_button.pack(side="left", padx=(0, 5))

        delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task)
        delete_button.pack(side="left", padx=(0, 5))

        clear_button = tk.Button(button_frame, text="Clear All", command=self.clear_all)
        clear_button.pack(side="left", padx=(0, 5))

    def add_task_event(self, event):
        self.add_task()

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if not task_text:
            messagebox.showwarning("Warning", "Task description cannot be empty.")
            return

        self.tasks_listbox.insert(tk.END, task_text)
        self.task_entry.delete(0, tk.END)

    def mark_done(self):
        index = self.tasks_listbox.curselection()
        if not index:
            messagebox.showinfo("Info", "Select a task to mark as done.")
            return

        i = index[0]
        text = self.tasks_listbox.get(i)

        # If not already marked, prefix with [DONE]
        if not text.startswith("[DONE] "):
            self.tasks_listbox.delete(i)
            self.tasks_listbox.insert(i, "[DONE] " + text)

    def delete_task(self):
        index = self.tasks_listbox.curselection()
        if not index:
            messagebox.showinfo("Info", "Select a task to delete.")
            return
        self.tasks_listbox.delete(index[0])

    def clear_all(self):
        if messagebox.askyesno("Confirm", "Delete all tasks?"):
            self.tasks_listbox.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskListApp(root)
    root.mainloop()
