from tkinter import *
from tkinter import ttk
root = Tk()
l =ttk.label(root, text="starting...")
l.grid()
l.bind('<Enter>', lambda e: l.configure(text='moved mouse inside'))
l.bind('<Enter>', lambda e: l.configure(text='moved mouse outside'))
l.bind('<ButtonPress-1>', lambda e: l.configure(text='clicked left mouse button'))
l.bind('<3>',lambda e: l.configure('clicked thirt mouse button'))
l.bind('<Double-1>', lambda e: l.configure(text='Double Clicked'))
l.bind('<B3-Motion>', lambda e: l.configure(text=f'third button to {e.x}, {e.y}'))
root.mainloop