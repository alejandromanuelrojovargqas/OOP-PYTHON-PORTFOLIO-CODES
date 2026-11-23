from tkinter import *
from tkinter import ttk

root = Tk()

# Fila 0: Lista
l = Listbox(root, height=5)
l.grid(column=0, row=0, sticky=(N,W,E,S))

# Fila 1: Scrollbar horizontal
s = ttk.Scrollbar(root, orient=HORIZONTAL, command=l.xview)
s.grid(column=0, row=1, sticky=(E,W))
l['xscrollcommand'] = s.set

# Fila 2: Etiqueta de estado (se cambió row=1 a row=2)
ttk.Label(root, text="Status message here", anchor=(W)).grid(column=0, columnspan=2, row=2, sticky=(W,E))

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Insertar líneas con texto suficientemente largo
for i in range(1, 101):
    l.insert('end', f"Línea {i} de 100 con texto largo para probar el desplazamiento horizontal")

root.mainloop()