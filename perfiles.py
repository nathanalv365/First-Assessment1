import tkinter as tk
from tkinter import ttk, messagebox

def aplicar_descuentos(total, var_tarjeta, var_seguro, var_fidelizacion,
                       carrito):
  descuento_total = 0

  if var_tarjeta.get():  # Corregido para obtener el valor booleano
    descuento_total += 10  # Descuento del 10% por tener tarjeta de crédito
  if var_seguro.get():  # Corregido para obtener el valor booleano
    descuento_total += 5  # Descuento del 5% por tener seguro
  if var_fidelizacion.get():  # Corregido para obtener el valor booleano
    descuento_total += 15  # Descuento del 15% por participar en programa de fidelización

  total_con_descuento = total * (1 - descuento_total / 100)

  messagebox.showinfo(
      "Descuentos Aplicados",
      f"Se aplicó un descuento del {descuento_total}%. Total a pagar: ${total_con_descuento:.2f}"
  )
  return total_con_descuento
