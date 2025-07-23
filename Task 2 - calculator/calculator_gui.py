
---

### 🧾 `Task 2 - Calculator/calculator_gui.py`

Here’s the clean, rounded-edge, spaced version:

```python
import tkinter as tk

def click(event):
    current = str(entry.get())
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.geometry("320x450")
root.title("Calculator")
root.configure(bg="#F2F2F2")  # Soft background

# Entry field
entry = tk.Entry(root, font="Arial 24", bd=2, relief="solid", justify="right", bg="white")
entry.pack(pady=20, padx=15, fill=tk.BOTH, ipadx=8, ipady=10)

# Button layout
buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "=", "/"]
]

# Styles
btn_bg = "#ffffff"
btn_fg = "#333333"
btn_font = ("Arial", 18)
btn_active = "#DDE6ED"
btn_border = "#cccccc"

for row in buttons:
    row_frame = tk.Frame(root, bg="#F2F2F2")
    row_frame.pack(pady=5)
    for btn in row:
        b = tk.Button(
            row_frame, text=btn,
            font=btn_font,
            fg=btn_fg,
            bg=btn_bg,
            activebackground=btn_active,
            relief="flat",
            width=4, height=2,
            bd=2,
            highlightbackground=btn_border,
            highlightthickness=1,
            padx=8,
            pady=6
        )
        b.pack(side=tk.LEFT, padx=8)
        b.bind("<Button-1>", click)

root.mainloop()
