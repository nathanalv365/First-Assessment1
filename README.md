Tienda Online

Este es un sistema de tienda online desarrollado en Python utilizando la biblioteca Tkinter para la interfaz gráfica de usuario. Permite a los usuarios iniciar sesión, registrar nuevas cuentas, navegar por productos, agregar productos al carrito de compras, ver el carrito y realizar pagos.
Funcionalidades
Autenticación de Usuarios

    Inicio de Sesión: Los usuarios pueden iniciar sesión con sus credenciales existentes. Se realiza una validación de las credenciales ingresadas para garantizar la seguridad del acceso.
    Registro de Nuevos Usuarios: Los nuevos usuarios pueden registrar cuentas proporcionando un nombre de usuario y una contraseña. Se realiza una verificación para evitar registros duplicados.

Exploración y Compra de Productos

    Navegación de Productos: Los productos se muestran organizados por categorías, lo que facilita a los usuarios la búsqueda de productos específicos.
    Productos en Promoción: Los productos que están en promoción se destacan con etiquetas especiales para llamar la atención de los usuarios sobre las ofertas disponibles.
    Agregado al Carrito: Los usuarios pueden agregar productos al carrito de compras con un solo clic desde la interfaz de usuario.

Gestión del Carrito de Compras

    Visualización del Carrito: Los usuarios pueden ver los productos que han agregado al carrito de compras, así como el total de la compra.
    Procesamiento de Pagos: Los usuarios pueden proceder al pago de los productos en el carrito. Se aplican descuentos según las promociones actuales y las opciones seleccionadas por el usuario.

Gestión de Perfiles de Usuario

    Perfil de Usuario: Los usuarios pueden acceder a un perfil donde pueden actualizar su nombre, dirección y preferencias financieras, como la participación en programas de fidelización o la posesión de tarjetas de crédito.

Estructura del Código

    main.py: Contiene el código principal para la interfaz gráfica de usuario y la lógica de interacción con el usuario.
    autenticacion.py: Contiene funciones relacionadas con la autenticación de usuarios, como la validación de credenciales y el registro de nuevos usuarios.
    productos.py: Define los productos disponibles para la venta, así como las promociones actuales.
    perfiles.py: Contiene funciones relacionadas con la gestión de perfiles de usuario, como la aplicación de descuentos.

Ejecución

Para ejecutar la aplicación, simplemente ejecuta el archivo main.py utilizando Python:

bash

python main.py

Se abrirá una ventana de interfaz gráfica donde los usuarios podrán interactuar con la tienda online.
Requisitos

    Python 3.x
    Tkinter (instalado por defecto en la mayoría de las distribuciones de Python)
