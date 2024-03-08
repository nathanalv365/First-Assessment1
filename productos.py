# productos.py
import random

# Lista de productos con precios
productos = {
    "Ropa": {"Camiseta": 10, "Pantalón": 20, "Vestido": 30},
    "Electrodomésticos": {"Nevera": 500, "Lavadora": 400, "Televisor": 300},
    "Hogar": {"Mesa": 50, "Silla": 25, "Sofá": 200}
}

# Productos en promoción
promocion = {"Pantalón": 15, "Televisor": 250, "Mesa": 40}

# Función para obtener todos los productos disponibles
def obtener_productos_disponibles():
    productos_disponibles = []
    for categoria, productos_categoria in productos.items():
        for producto, precio in productos_categoria.items():
            if producto in promocion:
                productos_disponibles.append(f"{categoria}: {producto} - ${promocion[producto]} (Promoción)")
            else:
                productos_disponibles.append(f"{categoria}: {producto} - ${precio}")
    return productos_disponibles


