# Diccionarios
Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}


def menu_principal():
    while True:
        mostrar_productos()
        print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
        opcion = input("Elija opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            eliminar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            print("Sesión finalizada correctamente.")
            break
        else:
            print("Error: Opción inválida.")
            
def mostrar_productos():
    print("=" * 60)
    print("Lista de Productos:")
    print("=" * 60)
    # Encabezados de columnas para diferenciar
    print(f"{'CÓDIGO':<10} {'NOMBRE':<20} {'PRECIO':<10} {'STOCK':<10}")
    print("-" * 60)
    for codigo in Productos:
        print(f"{codigo:<10} {Productos[codigo]:<20} {Precios[codigo]:<10.2f} {Stock[codigo]:<10}")
    print("=" * 60)

def agregar_producto():
    # Auto-incrementar ID de los codigos
    nuevo_codigo = max(Productos.keys()) + 1 if Productos else 1
    
    nombre = input("Ingrese nombre del producto: ")
    
    # Validación de precio agregar el precio
    while True:
        try:
            precio = float(input("Ingrese precio del producto: "))
            if precio <= 0:
                print("El precio debe ser mayor que cero.")
                continue
            break
        except ValueError:
            print("Formato inválido. Intente nuevamente.")
    
    # Validación de stock agregar el stock
    while True:
        try:
            cantidad = int(input("Ingrese cantidad en stock: "))
            if cantidad < 0:
                print("El stock no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Formato inválido. Ingrese un número entero.")
    
    # Persistencia de datos en diccionarios
    Productos[nuevo_codigo] = nombre
    Precios[nuevo_codigo] = precio
    Stock[nuevo_codigo] = cantidad
    
    print(f"Producto '{nombre}' agregado con código {nuevo_codigo}.")

def eliminar_producto():
    codigo = input("Ingrese el código del producto a eliminar: ")
    
    try:
        codigo = int(codigo)
        if codigo in Productos:
            nombre = Productos[codigo]
            del Productos[codigo]
            del Precios[codigo]
            del Stock[codigo]
            print(f"Producto '{nombre}' eliminado del sistema.")
        else:
            print(f"Error: Código {codigo} no encontrado en el sistema.")
    except ValueError:
        print("Error: Código inválido.")

def actualizar_producto():
    codigo = input("Ingrese el código del producto a actualizar: ")
    
    try:
        codigo = int(codigo)
        if codigo in Productos:
            print(f"Actualizando: {codigo} {Productos[codigo]} {Precios[codigo]} {Stock[codigo]}")
            
            print("\nOpciones de actualización:")
            print("[1] Nombre")
            print("[2] Precio")
            print("[3] Stock")
            opcion = input("Seleccione campo a modificar: ")
            
            if opcion == "1":
                nuevo_nombre = input("Nuevo nombre: ")
                Productos[codigo] = nuevo_nombre
                print("Registro actualizado.")
            
            elif opcion == "2":
                try:
                    nuevo_precio = float(input("Nuevo precio: "))
                    if nuevo_precio <= 0:
                        print("Error: El precio debe ser mayor que cero.")
                    else:
                        Precios[codigo] = nuevo_precio
                        print("Registro actualizado.")
                except ValueError:
                    print("Error: Formato de precio inválido.")
            
            elif opcion == "3":
                try:
                    nuevo_stock = int(input("Nuevo stock: "))
                    if nuevo_stock < 0:
                        print("Error: Stock no puede ser negativo.")
                    else:
                        Stock[codigo] = nuevo_stock
                        print("Registro actualizado.")
                except ValueError:
                    print("Error: Formato de stock inválido.")
            
            else:
                print("Opción no reconocida.")
        else:
            print(f"Error: Código {codigo} no existe en el sistema.")
    except ValueError:
        print("Error: Formato de código inválido.")

if __name__ == "__main__":
    menu_principal()