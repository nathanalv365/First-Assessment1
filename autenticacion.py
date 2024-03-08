# autenticacion.py
import tkinter as tk
from tkinter import ttk, messagebox
# Lista para almacenar usuarios registrados
usuarios_registrados = []

def validar_credenciales(usuario, contrasena):
    if (usuario, contrasena) in usuarios_registrados:
        return True
    else:
        return False

def registrar_usuario(usuario, contrasena):
    if (usuario, contrasena) not in usuarios_registrados:
        usuarios_registrados.append((usuario, contrasena))
        return True
    else:
        return False