# main.py
import tkinter as tk
from tkinter import ttk, messagebox
from ui import iniciar_sesion, registrar

root = tk.Tk()
root.title("Bienvenido")

# Elementos de la ventana de inicio de sesión y registro
label_usuario = ttk.Label(root, text="Usuario:")
label_usuario.grid(row=0, column=0, padx=5, pady=5)
entry_usuario = ttk.Entry(root)
entry_usuario.grid(row=0, column=1, padx=5, pady=5)

label_contrasena = ttk.Label(root, text="Contraseña:")
label_contrasena.grid(row=1, column=0, padx=5, pady=5)
entry_contrasena = ttk.Entry(root, show="*")
entry_contrasena.grid(row=1, column=1, padx=5, pady=5)

boton_inicio_sesion = ttk.Button(root, text="Iniciar Sesión", command=iniciar_sesion)
boton_inicio_sesion.grid(row=2, column=0, padx=5, pady=5)

boton_registro = ttk.Button(root, text="Registrarse", command=registrar)
boton_registro.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()