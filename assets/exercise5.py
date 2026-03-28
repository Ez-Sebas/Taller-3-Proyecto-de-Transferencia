# Flujo recomendado para refactorizar (con pruebas)
# 1.Entender el comportamiento actual
# 2.Crear pruebas que describan ese comportamiento
# 3.Refactorizar en pasos pequeños:
# * Renombrar
# * Extraer funciones
# * Eliminar duplicación
# * Separar I/O de lógica
# 4.Ejecutar pruebas a cada paso
# 5.Al final: revisar estilo (PEP8), tipado, docstrings

# 🧩 Ejercicio 5: 
# Refactorizar validador de contraseñas (legibilidad + mantenibilidad + pruebas)
# Código inicial (mejorable)

def tiene_longitud_minima(contrasena: str) -> bool:
    return len(contrasena) >= 8

def tiene_mayuscula(contrasena: str) -> bool:
    return any(c.isupper() for c in contrasena)

def tiene_numero(contrasena: str) -> bool:
    return any(c.isdigit() for c in contrasena)

def no_tiene_espacios(contrasena: str) -> bool:
    return " " not in contrasena

def obtener_errores(contrasena: str) -> list:
    errores = []
    
    if not tiene_longitud_minima(contrasena):
        errores.append("Debe Tener al Menos 8 Caracteres.")
    if not tiene_mayuscula(contrasena):
        errores.append("Debe Tener al Menos una Letra en Mayuscula.")
    if not tiene_numero(contrasena):
        errores.append("Debe Tener al Menos un Numero.")
    if not no_tiene_espacios(contrasena):
        errores.append("No Debe Contener Espacios en Blanco.")
        
    return errores

def validar_contrasena(contrasena: str) -> bool:
    return len(obtener_errores(contrasena)) == 0

def main():
    contrasena = input("Ingrese una Contraseña: ")
    errores = obtener_errores(contrasena)
    
    if not errores:
        print("Contraseña Válida")
    else:
        print("Contraseña Inválida. Aspectos que no se Cumplen:")
        for error in errores:
            print(f"  - {error}")
            
if __name__ == "__main__":
    main()