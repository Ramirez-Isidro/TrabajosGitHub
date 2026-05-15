import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()

año_actual = simpledialog.askinteger("Datos", "Ingrese el año actual:")
edad = simpledialog.askinteger("Datos", "Ingrese su edad:")

año_nacimiento = año_actual - edad

messagebox.showinfo("Resultado", f"usted nacio en el año: {año_nacimiento}")