# gestor-inventario-listas

# Objetivo

Este programa es un gestor de inventario para una tienda pequeña, y sirve para registrar productos con su cantidad, consultarlos, modificarlos y eliminarlos, con el fin de practicar el manejo de listas, ciclos, condicionales y funciones en Python.

# Requisitos para ejecutar el programa

Se necesita tener Python 3 instalado en el computador y, para ejecutarlo como se hice yo por medio de Visual Studio Code con la extensión de Python y el programa no usa librerías externas, archivos ni bases de datos.

# Instrucciones de uso

Para usar el programa se descarga el archivo main.py y se abre en Visual Studio Code, y allí se ejecuta presionando el botón de **Run Python File** (el triángulo de la parte superior derecha) o abriendo la terminal integrada desde el menú **Terminal > New Terminal** y escribiendo `python main.py` y al ejecutarlo aparece un menú con ocho opciones numeradas, y para elegir una se escribe su número en la terminal y se presiona Enter, tras lo cual el programa pide los datos que necesite, como el nombre del producto o la cantidad tambien el menú se repite después de cada acción hasta que se elige la opción 8 para salir, y los datos se pierden al cerrar el programa porque no se guardan en ningún archivo.

# Funciones implementadas

- buscar_indice: busca un producto por su nombre, sin importar mayúsculas ni espacios, y devuelve -1 si no existe.
- registrar_producto: agrega un producto y su cantidad, siempre que no esté ya registrado.
- mostrar_inventario: muestra todos los productos con su cantidad.
- buscar_producto: consulta un producto por su nombre.
- modificar_cantidad: cambia la cantidad de un producto que exista.
- eliminar_producto: elimina un producto de las dos listas a la vez.
- mostrar_resumen: muestra cuántos productos diferentes hay.
- mostrar_mayor_cantidad: muestra el producto con más unidades.

# cómo se relacionan las listas

El programa usa dos listas paralelas, productos y cantidades, de modo que el producto que está en la posición i de la primera tiene su cantidad en la posición i de la segunda, y por eso cada vez que se agrega o se elimina un producto el cambio se hace en las dos listas con el mismo índice.

# Productos repetidos

Para evitar registrar dos veces el mismo producto, el programa usa la función buscar_indice, que registrar_producto llama antes de agregar algo nuevo, y así revisa si el nombre ya existe sin importar las mayúsculas ni los espacios de más, de manera que si el producto ya está registrado no se agrega y se le avisa al usuario, con lo cual cada producto aparece una sola vez y los datos no se enredan.

# PRUEBAS 

Registrar tres productos con cantidades diferentes

<img width="585" height="721" alt="image" src="https://github.com/user-attachments/assets/2ddd8361-a808-4b51-ad7c-649363af3109" />


Mostrar el inventario completo

<img width="349" height="244" alt="image" src="https://github.com/user-attachments/assets/642427e1-f34d-46f4-9f8d-53982fe112fa" />

Buscar un producto que exista y otro que no exista

<img width="288" height="459" alt="image" src="https://github.com/user-attachments/assets/de4f7e9c-a61d-41c6-b3f1-5c409a7eef92" />

Modificar la cantidad de un producto

<img width="329" height="479" alt="image" src="https://github.com/user-attachments/assets/00bfd6cf-d9a6-4314-a267-93ac72873f88" />


Eliminar el primer producto y comprobar que las listas siguen sincronizadas.

<img width="305" height="449" alt="image" src="https://github.com/user-attachments/assets/b8523235-993a-4acb-a10f-2f9034e58852" />


 Intentar eliminar un producto inexistente.

<img width="291" height="234" alt="image" src="https://github.com/user-attachments/assets/3768a335-3e6c-46d7-84a2-aeafd682d538" />

Consultar el resumen cuando el inventario tiene datos

<img width="290" height="416" alt="image" src="https://github.com/user-attachments/assets/c7b1db3a-942a-459a-aaf2-c354f538430f" />

Consultar el inventario vacío.

<img width="324" height="411" alt="image" src="https://github.com/user-attachments/assets/4900d3d2-3580-4c9c-a09e-c044a9400995" />




