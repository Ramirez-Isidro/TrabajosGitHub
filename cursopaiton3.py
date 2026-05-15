import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()

nombre = simpledialog.askstring("Datos", "Ingrese su nombre:")
deporte = simpledialog.askstring("Datos", "que deporte practica?:")

messagebox.showinfo("datos",f"Bienvenido/a {nombre}, que bueno que entrenes {deporte} en Villa Mitre."  )