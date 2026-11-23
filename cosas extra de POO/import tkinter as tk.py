import tkinter as tk

root = tk.Tk()
txt = tk.Text(root, height=5, width=40)
txt.pack()

# Insert some lines
for i in range(1, 21):
    txt.insert(tk.END, f"Line {i}\n")

# Scroll to line 5
txt.see(1.0) # "line.column" format, so "5.0" means line 5, column 0

root.mainloop()