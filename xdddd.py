from tkinter import *
from tkinter import ttk

root = Tk()

# 1. Configuración del límite y variable
MAX_LIMIT = 5
texto_var = StringVar()

# 2. Función que recorta texto y actualiza el contador
def al_cambiar_texto(*args):
    texto = texto_var.get()
    if len(texto) > MAX_LIMIT:
        texto_var.set(texto[:MAX_LIMIT])
        texto = texto[:MAX_LIMIT]
    lbl_contador.config(text=f"{len(texto)}/{MAX_LIMIT}")

# 3. Vincular el evento
texto_var.trace_add("write", al_cambiar_texto)

# 4. Creación de componentes
content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
namelbl = ttk.Label(content, text="introduce tu nametag")

# Entry único conectado a texto_var
name = ttk.Entry(content, textvariable=texto_var)

# Label del contador
lbl_contador = ttk.Label(content, text=f"0/{MAX_LIMIT}")

onevar = BooleanVar(value=False)
one = ttk.Checkbutton(content, text="estoy de acuerdo con los terminos y condiciones", variable=onevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

# 5. Posicionamiento en el Grid
content.grid(column=0, row=0, sticky=(N,S,E,W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N,S,E,W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N,E,W), pady=5, padx=5)
name.grid(column=3, row=1, columnspan=2, sticky=(N,E,W))
lbl_contador.grid(column=3, row=2, columnspan=2, sticky=(E), padx=5) # Muestra el contador debajo del Entry

one.grid(column=0, row=5, sticky=(S,E,W))
ok.grid(column=3, row=5, sticky=(S,E,W))
cancel.grid(column=4, row=5, sticky=(S,E,W))

# --- CONFIGURACIÓN DE REDIMENSIONAMIENTO (ESTIRAR PANTALLA) ---
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()