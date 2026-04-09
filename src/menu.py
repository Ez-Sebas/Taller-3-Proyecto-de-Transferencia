# menu.py
# Punto de entrada del programa — Módulo 1

from service import new_register, list_records, search_record, update_record, delete_record
from colorama import init, Fore, Style, Back

init(autoreset=True)


def mostrar_menu():
    print("\n" + Fore.RED + "========================================")
    print(Fore.YELLOW + "SISTEMA DE GESTIÓN DE USUARIOS")
    print(Fore.RED +"========================================")
    print(Fore.YELLOW + "  1. Crear usuario")
    print(Fore.YELLOW + "  2. Listar usuarios")
    print(Fore.YELLOW + "  3. Buscar usuario")
    print(Fore.YELLOW + "  4. Actualizar usuario")
    print(Fore.YELLOW + "  5. Eliminar usuario")
    print(Fore.YELLOW +"  0. Salir")
    print(Fore.RED +"========================================")


def solicitar_usuario():
    
    """Pide los datos del nuevo usuario por consola y llama a crear_usuario."""
    
    print(Fore.RED +"\n── Nuevo usuario ──")
    id_input = input(Fore.GREEN + "ID: ").strip()
    nombre_input = input(Fore.GREEN + "Nombre: ").strip()
    correo_input = input(Fore.GREEN + "Correo: ").strip()
    edad_input = input(Fore.GREEN + "Edad: ").strip()
    estado_input = input(Fore.GREEN + "Estado: ").strip()
    
    exito, mensaje = new_register(id_input, nombre_input, correo_input, edad_input, estado_input)
    
    if exito:
        print(Fore.GREEN + f"\n {mensaje}")
    else:
        print(Fore.RED + "\n Se encontraron los siguientes errores:")
        for error in mensaje:
            print(f"   • {error}")


def mostrar_usuarios():
    
    """Lista todos los usuarios registrados en memoria."""
    
    print(Fore.YELLOW + "\n── Usuarios registrados ──")
    resumen = list_records()
    
    if not resumen:
        print(Fore.YELLOW + "No hay usuarios registrados aún.")
    else:
        for linea in resumen:
            print(" •", linea)


def buscar_usuario():
    """Busca usuario por ID e imprime su información."""
    
    id_input = input(Fore.GREEN + "ID: ").strip()
    exito, mensaje = search_record(id_input)
    
    if exito:
        print(Fore.GREEN + f"\n {mensaje}")
    else:
        print(Fore.RED + f"\n {mensaje}")


def actualizar_usuario():
    
    """Pide el ID del usuario a actualizar y los nuevos datos."""
    
    id_input = input(Fore.GREEN + "ID: ").strip()
    nombre_input = input(Fore.GREEN + "Nombre: ").strip()
    correo_input = input(Fore.GREEN + "Correo: ").strip()
    edad_input = input(Fore.GREEN + "Edad: ").strip()
    estado_input = input(Fore.GREEN + "Estado: ").strip()
    
    exito, mensaje = update_record(id_input, nombre_input, correo_input, edad_input, estado_input)
    
    if exito:
        print(Fore.GREEN + f"\n {mensaje}")
    else:
        print(Fore.RED + "\n Se encontraron los siguientes errores:")
        for error in mensaje:
            print(f"   • {error}")


def eliminar_usuario():
    """Pide el ID del usuario a eliminar."""
    
    id_input = input(Fore.GREEN + "ID: ").strip()
    exito, mensaje = delete_record(id_input)
    
    if exito:
        print(Fore.GREEN + f"\n {mensaje}")
    else:
        print(Fore.RED + f"\n {mensaje}")


def main():
    print("Sistema listo")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Elige una opción: ").strip()
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido. ¡Hasta luego!")
            break
        
        if opcion == "1":
            solicitar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            buscar_usuario()
        elif opcion == "4":
            actualizar_usuario()
        elif opcion == "5":
            eliminar_usuario()
        elif opcion == "0":
            print("\n¡Hasta luego!")
            break
        else:
            print("\n Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()