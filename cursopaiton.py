import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()

nombre = simpledialog.askstring("socio", "Ingrese su nombre:")
edad = simpledialog.askinteger("socio", "Ingrese su edad:")
peso = simpledialog.askfloat("socio", "Ingrese su peso en kg (use punto en lugar de coma):")
cuota = simpledialog.askfloat("socio", "Ingrese el valor de la cuota mensual:")

recargo = 500
total_pagar = cuota + recargo

apto_fisico = True

messagebox.showinfo("proceso completado", f"Bienvenido/a {nombre} al gimnasio del Club Villa Mitre.")
messagebox.showinfo("cuota", f"total a pagar: ${total_pagar}")
estado_apto = "Sí" if apto_fisico else "No"
messagebox.showinfo("Estas apto?", f" {estado_apto}, hora de entrenar.")