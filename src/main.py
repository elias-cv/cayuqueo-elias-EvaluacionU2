from modelos import Equipo, Estudiantes, Prestamos
from crud_equipos import crear_equipo, listar_equipos, buscar_equipo_id, actualizar_equipo, eliminar_equipo

def menu():
    print("=== Menú de Gestión de Equipos ===")
    print("1. Crear equipo")
    print("2. Listar equipos")
    print("3. Buscar equipo por ID")
    print("4. Actualizar equipo")
    print("5. Eliminar equipo")
    print("6. Crear préstamo")
    print("7. Listar préstamos")
    print("8. Devolver préstamo")
    print("0. Salir")

def main_crear_equipo():
    nombre = input("Ingrese el nombre del equipo: ")
    tipo = input("Ingrese el tipo del equipo: ")
    stock_disponible = int(input("Ingrese el stock disponible: "))
    try:
        equipo = crear_equipo(nombre, tipo, stock_disponible)
        print(f"Equipo creado con ID: {equipo.id}")
    except ValueError as e:
        print(f"Error: {e}")

def main_listar_equipos():
    equipos = listar_equipos()
    if not equipos:
        print("No hay equipos registrados.")
    else:
        for equipo in equipos:
            print(f"ID: {equipo.id}, Nombre: {equipo.nombre}, Tipo: {equipo.tipo}, Stock Disponible: {equipo.stock_disponible}")

def main_buscar_equipo():
    id_equipo = int(input("Ingrese el ID del equipo a buscar: "))
    try:
        equipo = buscar_equipo_id(id_equipo)
        print(f"ID: {equipo.id}, Nombre: {equipo.nombre}, Tipo: {equipo.tipo}, Stock Disponible: {equipo.stock_disponible}")
    except ValueError as e:
        print(f"Error: {e}")


def main_actualizar_equipo():
    id_equipo = int(input("Ingrese el ID del equipo a actualizar: "))
    nombre = input("Ingrese el nuevo nombre del equipo (dejar en blanco para no cambiar): ")
    tipo = input("Ingrese el nuevo tipo del equipo (dejar en blanco para no cambiar): ")
    stock_disponible_input = input("Ingrese el nuevo stock disponible (dejar en blanco para no cambiar): ")
    stock_disponible = int(stock_disponible_input) if stock_disponible_input else None
    try:
        equipo = actualizar_equipo(id_equipo, nombre or None, tipo or None, stock_disponible)
        print(f"Equipo actualizado: ID: {equipo.id}, Nombre: {equipo.nombre}, Tipo: {equipo.tipo}, Stock Disponible: {equipo.stock_disponible}")
    except ValueError as e:
        print(f"Error: {e}")

def main_eliminar_equipo():
    id_equipo = int(input("Ingrese ID del equipo a eliminar: "))
    try:
        eliminar_equipo(id_equipo)
        print(f"Equipo con ID {id_equipo} eliminado exitosamente.")
    except ValueError as e:
        print(f"Error: {e}")

def main_crear_prestamo():
    from prestamos import crear_prestamo
    equipo_id = int(input("Ingrese el ID del equipo a prestar: "))
    estudiante_id = int(input("Ingrese el ID del estudiante que realiza el préstamo: "))
    cantidad = int(input("Ingrese la cantidad a prestar: "))
    try:
        prestamo = crear_prestamo(equipo_id, estudiante_id, cantidad)
        print(f"Préstamo creado con ID: {prestamo.id}, Fecha: {prestamo.fecha}, Cantidad: {prestamo.cantidad}")
    except ValueError as e:
        print(f"Error: {e}")

def main_listar_prestamos():
    from prestamos import listar_prestamos
    prestamos = listar_prestamos()
    if not prestamos:
        print("No hay préstamos registrados.")
    else:
        for prestamo in prestamos:
            estado = "Activo" if prestamo.estado else "Devuelto"
            print(f"ID: {prestamo.id}, Fecha: {prestamo.fecha}, Cantidad: {prestamo.cantidad}, Estado: {estado}, Equipo: {prestamo.equipo.nombre}, Estudiante: {prestamo.estudiante.nombre}")

def main_devolver_prestamo():
    from prestamos import devolver_prestamo
    prestamo_id = int(input("Ingrese el ID del préstamo a devolver: "))
    try:
        prestamo = devolver_prestamo(prestamo_id)
        print(f"Préstamo con ID {prestamo.id} devuelto exitosamente.")
    except ValueError as e:
        print(f"Error: {e}")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            main_crear_equipo()
        elif opcion == "2":
            main_listar_equipos()
        elif opcion == "3":
            main_buscar_equipo()
        elif opcion == "4":
            main_actualizar_equipo()
        elif opcion == "5":
            main_eliminar_equipo()
        elif opcion == "6":
            main_crear_prestamo()
        elif opcion == "7":
            main_listar_prestamos()
        elif opcion == "8":
            main_devolver_prestamo()
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")