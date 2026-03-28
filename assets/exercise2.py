# Ejercicio 2 Abrir un archivo, capturar errores de apertura, contar lineas en else, cerrar en finally y mostrar un mnesaje final 

route = "datos.txt"
file = None

try:
    file = open(route, "r", encoding="utf-8")
    
except Exception as e:
    print(f"No se pudo abrir el archivo: {e}")
else:
    print(f"Líenas en el archivo: {sum(1 for _ in file)}")
    
finally:
    if file:
        file.close()
        print("Fin del programa.")