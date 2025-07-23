
import tkinter as tk
from tkinter import messagebox

class HoverButton(tk.Button):
    def __init__(self, master=None, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.default_bg = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self["background"] = "#5C8374"  # Hover color

    def on_leave(self, e):
        self["background"] = self.default_bg

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("380x460")
        self.root.config(bg="#EEF7F3")
        self.root.resizable(False, False)

        self.tasks = []

        title = tk.Label(root, text="My Tasks 📝", font=("Arial", 18, "bold"), bg="#EEF7F3", fg="#3A4D39")
        title.pack(pady=(20, 5))

        self.frame = tk.Frame(root, bg="#EEF7F3")
        self.frame.pack(pady=10)

        self.entry = tk.Entry(self.frame, width=26, font=("Arial", 12), bd=2, relief="solid")
        self.entry.pack(side=tk.LEFT, padx=(0, 10))

        self.add_button = HoverButton(self.frame, text="Add", width=8, bg="#3A4D39", fg="white", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.task_frame = tk.Frame(root, bg="#EEF7F3")
        self.task_frame.pack(pady=10)

        self.task_widgets = []

        self.delete_btn = HoverButton(root, text="🗑️ Delete Selected", width=20, bg="#A34343", fg="white", command=self.delete_selected)
        self.delete_btn.pack(pady=15)

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            var = tk.IntVar()
            cb = tk.Checkbutton(
                self.task_frame,
                text=task_text,
                variable=var,
                font=("Arial", 11),
                bg="#EEF7F3",
                activebackground="#EEF7F3",
                anchor='w',
                selectcolor="#90C8AC",
                fg="#3A4D39"
            )
            cb.pack(fill='x', padx=20, pady=2, anchor='w')
            self.task_widgets.append((cb, var))
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task")

    def delete_selected(self):
        new_widgets = []
        for cb, var in self.task_widgets:
            if var.get() == 0:
                new_widgets.append((cb, var))
            else:
                cb.destroy()
        self.task_widgets = new_widgets

# Launch App
root = tk.Tk()
app = TodoApp(root)
root.mainloop()
