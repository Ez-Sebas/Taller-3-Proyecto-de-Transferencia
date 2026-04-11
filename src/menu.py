from service import new_register, list_records, search_record, update_record, delete_record, delete_all
from integration import generar_datos_falsos
from colorama import init, Fore, Style, Back

init(autoreset=True)


def mostrar_menu() -> None:
    """
    Muestra el menú principal en consola.
    """
    print("\n" + Fore.RED + "========================================")
    print(Fore.YELLOW + "SISTEMA DE GESTIÓN DE USUARIOS")
    print(Fore.RED +"========================================")
    print(Fore.YELLOW + "  1. Crear usuario")
    print(Fore.YELLOW + "  2. Listar usuarios")
    print(Fore.YELLOW + "  3. Buscar usuario")
    print(Fore.YELLOW + "  4. Actualizar usuario")
    print(Fore.YELLOW + "  5. Eliminar usuario")
    print(Fore.YELLOW + "  6. Generar datos falsos")
    print(Fore.YELLOW +"  0. Salir")
    print(Fore.RED +"========================================")


def solicitar_usuario() -> None:
    """
    Pide los datos del nuevo usuario por consola y llama a crear_usuario.
    """
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


def mostrar_usuarios() -> None:
    """
    Lista todos los usuarios registrados en memoria.
    """
    print(Fore.YELLOW + "\n── Usuarios registrados ──")
    resumen = list_records()
    
    if not resumen:
        print(Fore.YELLOW + "No hay usuarios registrados aún.")
    else:
        for linea in resumen:
            print(" •", linea)


def buscar_usuario()  -> None:
    """
    Busca usuario por ID e imprime su información.
    """
    id_input = input(Fore.GREEN + "ID: ").strip()
    exito, mensaje = search_record(id_input)
    
    if exito:
        print(Fore.GREEN + f"\n {mensaje}")
    else:
        print(Fore.RED + f"\n {mensaje}")


def actualizar_usuario() -> None:
    """
    Pide el ID del usuario a actualizar y los nuevos datos.
    """
    id_input = input(Fore.GREEN + "ID: ").strip()
    nombre_input = input(Fore.GREEN + "Nombre: ").strip()
    correo_input = input(Fore.GREEN + "Correo: ").strip()
    edad_input = input(Fore.GREEN + "Edad: ").strip()
    estado_input = input(Fore.GREEN + "Estado: ").strip()
    
    exito, mensaje = update_record(id_input, nombre_input, correo_input, edad_input, estado_input)
    
    if exito:
        print(Fore.GREEN + f"\n {mensaje}")
    else:
        print(Fore.RED + f"\n {mensaje}")


def menu_eliminar() -> None:
    """
    Muestra el submenú de eliminación en consola.
    """
    print("\n" + Fore.RED + "========================================")
    print(Fore.YELLOW + "ELIMINAR USUARIOS")
    print(Fore.RED +"========================================")
    print(Fore.YELLOW + "  1. Eliminar por ID")
    print(Fore.YELLOW + "  2. Eliminar todos los usuarios")
    print(Fore.YELLOW + "  0. Volver")
    print(Fore.RED +"========================================")


def main_eliminar() -> None:
    """
    Controla el flujo del submenú de eliminación.
    """
    while True:
        menu_eliminar()
        
        try:
            opcion = input("Elige una opción: ").strip()
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido. ¡Hasta luego!")
            break
        
        if opcion == "1":
            eliminar_usuario()
        elif opcion == "2":
            eliminar_todo()
        elif opcion == "0":
            print("\nVolviendo al menú principal...")
            break
        else:
            print("\n Opción no válida. Intenta de nuevo.")


def eliminar_usuario() -> None:
    """
    Pide el ID del usuario a eliminar.
    """
    id_input = input(Fore.GREEN + "ID: ").strip()
    exito, mensaje = delete_record(id_input)
    
    if exito:
        print(Fore.GREEN + f"\n {mensaje}")
    else:
        print(Fore.RED + f"\n {mensaje}")


def eliminar_todo() -> None:
    """
    Solicita confirmación y elimina todos los usuarios.
    """
    confirmacion = input(Fore.YELLOW + "¿Estás seguro que quieres eliminar TODOS los usuarios? (s/n): ").strip().lower()
    
    if confirmacion == "s":
        exito, mensaje = delete_all()
        
        if exito:
            print(Fore.GREEN + f"\n {mensaje}")
        else:
            print(Fore.RED + f"\n {mensaje}")


def datos_falsos() -> None:
    """
    Llama a la función de generación de datos falsos y muestra el resultado.
    """
    exito, mensaje = generar_datos_falsos(cantidad=10)
    
    if exito:
        print(Fore.GREEN + f"\n {mensaje}")
    else:
        print(Fore.RED + f"\n {mensaje}")


def main() -> None:
    """
    Función principal que inicia el programa y controla el menú.
    """
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
            main_eliminar()
        elif opcion == "6":
            datos_falsos()
        elif opcion == "0":
            print("\n¡Hasta luego!")
            break
        else:
            print("\n Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()