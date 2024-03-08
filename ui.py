import tkinter as tk
from tkinter import ttk, messagebox
from autenticacion import validar_credenciales, registrar_usuario
from productos import productos, promocion
from perfiles import aplicar_descuentos

root = tk.Tk()
root.title("Bienvenido")

carrito = []  # Lista para almacenar los productos seleccionados

# Etiqueta del carrito de compras
label_carrito = None

def iniciar_sesion():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    if validar_credenciales(usuario, contrasena):
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso.")
        abrir_ventana_tienda()  # Abrir la ventana de la tienda
    else:
        messagebox.showerror("Error", "Credenciales inválidas.")

def registrar():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    if registrar_usuario(usuario, contrasena):
        messagebox.showinfo("Registro", "Usuario registrado correctamente.")
    else:
        messagebox.showerror("Error", "El usuario ya está registrado.")

def agregar_producto_al_carrito(categoria, producto, precio):
    carrito.append((categoria, producto, precio))
    messagebox.showinfo("Carrito", f"Se agregó {producto} al carrito de compras.")
    # Actualizar la etiqueta del carrito
    label_carrito.config(text=f"Carrito ({len(carrito)} productos)")

def mostrar_productos(frame_productos):
    for categoria, productos_categoria in productos.items():
        frame_categoria = ttk.Frame(frame_productos)
        frame_categoria.pack(side=tk.LEFT, padx=10, pady=10)

        ttk.Label(frame_categoria, text=categoria, font=("Helvetica", 12, "bold")).pack(anchor=tk.W)
        for producto, precio in productos_categoria.items():
            if producto in promocion:
                precio_promocion = promocion[producto]
                label_producto = ttk.Label(frame_categoria, text=f"{producto} - ${precio_promocion} (Promoción)")
            else:
                label_producto = ttk.Label(frame_categoria, text=f"{producto} - ${precio}")
            label_producto.pack(anchor=tk.W)
            boton_agregar = ttk.Button(frame_categoria, text="Agregar al Carrito", command=lambda cat=categoria, prod=producto, prec=precio: agregar_producto_al_carrito(cat, prod, prec))
            boton_agregar.pack(anchor=tk.W)

def abrir_ventana_tienda():
    global label_carrito  # Acceder a la variable global
    ventana_tienda = tk.Toplevel(root)
    ventana_tienda.title("Tienda")
    ventana_tienda.geometry("600x400")  # Tamaño personalizado

    label_tienda = ttk.Label(ventana_tienda, text="¡Bienvenido a la Tienda!", font=("Helvetica", 16, "bold"))
    label_tienda.pack(pady=10)

    # Frame para el carrito de compras
    frame_carrito = ttk.Frame(ventana_tienda)
    frame_carrito.pack(pady=10, padx=10, fill=tk.BOTH)

    label_carrito = ttk.Label(frame_carrito, text="Carrito de Compras", font=("Helvetica", 12, "bold"))
    label_carrito.grid(row=0, column=0, columnspan=2, pady=10)

    # Botón para ver el carrito de compras
    boton_carrito = ttk.Button(frame_carrito, text="Ver Carrito", command=abrir_ventana_carrito)
    boton_carrito.grid(row=1, column=0, columnspan=2, pady=10)

    # Frame para los productos
    frame_productos = ttk.Frame(ventana_tienda)
    frame_productos.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    mostrar_productos(frame_productos)

    # Botón para abrir la ventana de perfil
    boton_perfil = ttk.Button(frame_carrito, text="Perfil", command=abrir_ventana_perfil)
    boton_perfil.grid(row=2, column=0, columnspan=2, pady=10)

def abrir_ventana_carrito():
    ventana_carrito = tk.Toplevel(root)
    ventana_carrito.title("Carrito de Compras")

    total = sum(precio for _, _, precio in carrito)

    label_carrito = ttk.Label(ventana_carrito, text="Carrito de Compras", font=("Helvetica", 16, "bold"))
    label_carrito.grid(row=0, column=0, columnspan=2, pady=10)

    for i, (categoria, producto, precio) in enumerate(carrito, start=1):
        ttk.Label(ventana_carrito, text=f"{i}. {categoria}: {producto} - ${precio}").grid(row=i, column=0, padx=5, pady=5)

    ttk.Label(ventana_carrito, text=f"Total: ${total}").grid(row=len(carrito)+1, column=0, columnspan=2, pady=10)

    # Supongamos que var_tarjeta, var_seguro y var_fidelizacion son variables tk.BooleanVar()
    var_tarjeta = tk.BooleanVar()
    var_seguro = tk.BooleanVar()
    var_fidelizacion = tk.BooleanVar()

    # Botón para procesar el pago
    ttk.Button(ventana_carrito, text="Pagar", command=lambda: procesar_pago(ventana_carrito, var_tarjeta, var_seguro, var_fidelizacion)).grid(row=len(carrito)+2, column=0, columnspan=2, pady=10)

def procesar_pago(ventana, var_tarjeta, var_seguro, var_fidelizacion):
    total = sum(precio for _, _, precio in carrito)  # Corregido para obtener solo los precios del carrito

    # Llama a la función aplicar_descuentos con los valores apropiados
    total_con_descuento = aplicar_descuentos(total, var_tarjeta, var_seguro, var_fidelizacion, carrito)
    
    ventana.destroy()
    carrito.clear()
    return total_con_descuento
  
nombre_usuario = ""
direccion_usuario = ""
tiene_tarjeta = False
tiene_seguro = False
tiene_fidelizacion = False

def guardar_cambios_perfil(entry_nombre, entry_direccion, var_tarjeta, var_seguro, var_fidelizacion):
      global nombre_usuario, direccion_usuario, tiene_tarjeta, tiene_seguro, tiene_fidelizacion
      nombre_usuario = entry_nombre.get()
      direccion_usuario = entry_direccion.get()
      tiene_tarjeta = var_tarjeta.get()
      tiene_seguro = var_seguro.get()
      tiene_fidelizacion = var_fidelizacion.get()

def abrir_ventana_perfil():
    ventana_perfil = tk.Toplevel(root)
    ventana_perfil.title("Perfil de Usuario")

    ttk.Label(ventana_perfil, text="Perfil de Usuario", font=("Helvetica", 16, "bold")).pack(pady=10)

    ttk.Label(ventana_perfil, text="Nombre:").pack()
    entry_nombre = ttk.Entry(ventana_perfil)
    entry_nombre.pack()
    entry_nombre.insert(0, nombre_usuario)

    ttk.Label(ventana_perfil, text="Dirección:").pack()
    entry_direccion = ttk.Entry(ventana_perfil)
    entry_direccion.pack()
    entry_direccion.insert(0, direccion_usuario)

    ttk.Label(ventana_perfil, text="Beneficios Financieros", font=("Helvetica", 12, "bold")).pack()

    var_tarjeta = tk.BooleanVar(value=tiene_tarjeta)
    var_seguro = tk.BooleanVar(value=tiene_seguro)
    var_fidelizacion = tk.BooleanVar(value=tiene_fidelizacion)

    ttk.Checkbutton(ventana_perfil, text="Tarjeta de Crédito", variable=var_tarjeta).pack()
    ttk.Checkbutton(ventana_perfil, text="Seguro", variable=var_seguro).pack()
    ttk.Checkbutton(ventana_perfil, text="Programa de Fidelización", variable=var_fidelizacion).pack()

    # Botón para guardar los cambios
    ttk.Button(ventana_perfil, text="Guardar Cambios", command=lambda: guardar_cambios_perfil(entry_nombre, entry_direccion, var_tarjeta, var_seguro, var_fidelizacion)).pack(pady=10)


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
