from tkinter import *
from tkinter import ttk

class feet_to_meters:
    def __init__(self,root):
        root.title("feets to meters")

        mainframe = ttk.frame(root,padding=(3,3,12,12))
        mainframe.grid(column=0 row=0, sticky=(N,W,E,S))

        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe,widh=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W,E))
        self.meters= StringVar()

        ttk.label(mainframe,textvariable=self.meters).grid(column=2, row=2, sticky=(W,E))
        ttk.button(mainframe, text="calculate", comand=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.label(mainframe,text="feet").grid(column=3, row=1, sticky=W)
        ttk.label(mainframe,text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.label(mainframe,text="meters").grid(column=3, row=2, sticky=W)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe.columnconfigure(2, weoght=1)
        for child in frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind("<return>", self.calculate)
    def calculate(self, *args):
        try:
            value = float(self.feet.get)
            self.meters.set(round(0.3048 * value))
        except ValueError:
            pass

root = tk()
FeetToMeters(root)
root.mainloop()