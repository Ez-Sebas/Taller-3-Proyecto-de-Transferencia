#Ejercicio 3:
#Crear un menú con: (1) dividir números, (2) abrir un archivo, (3) salir.
# Captura ValueError, ZeroDivisionError, FileNotFoundError y usa un except
# Exception final para no previstos.

route = "datos.txt"
file = None

while True:
    try:
        print("Menú:")
        print("1. Dividir números")
        print("2. Abrir un archivo")
        print("3. Salir")
        
        op = input("Selecciona una opción: ")
        
        match op:
            case "1":
                try:
                    num1 = float(input("Ingrese el primer número: "))
                    num2 = float(input("Ingrese el segundo número: "))
                    
                    resultado = num1 / num2
                    print(resultado)
                        
                except ZeroDivisionError as e:
                    print(f"No se puede dividir por cero: {e}")
            case "2":
                try:
                    file = open(route, "r", encoding="utf-8")
                    print(f"Líenas en el archivo: {sum(1 for _ in file)}")
                    
                except FileNotFoundError as e:
                    print(f"No se pudo abrir el archivo: {e}")
            case "3":
                print("Saliendo del programa.")
                break
            case "4":
                try:
                    raise ValueError("Opción no válida.")
                except ValueError as e:
                    print(f"Error capturado: {e}")
                
    except Exception as e:
        print(f"Ocurrió un error: {e}")