# service.py
# Módulo de lógica de negocio para la gestión de usuarios en memoria

from validate import (
    validar_id,
    validar_nombre,
    validar_correo,
    validar_edad,
    validar_estado,
)

from colorama import init, Fore, Style, Back
init(autoreset=True)

from file import load_data, save_data

usuarios = load_data()  # Lista de diccionarios: cada elemento es un usuario
ids_registrados = set([u["id"] for u in usuarios])  # Set para garantizar IDs únicos


def new_register(id, nombre, correo, edad, estado):
    """
    Recibe los campos del usuario, los valida y los guarda en memoria.
    """
    
    errores = []
    
    ok, id_val = validar_id(id, ids_registrados)
    if not ok:
        errores.append(id_val)

    ok, nombre_val = validar_nombre(nombre)
    if not ok:
        errores.append(nombre_val)

    ok, correo_val = validar_correo(correo)
    if not ok:
        errores.append(correo_val)

    ok, edad_val = validar_edad(edad)
    if not ok:
        errores.append(edad_val)

    ok, estado_val = validar_estado(estado)
    if not ok:
        errores.append(estado_val)
        
    if errores:
        return False, errores

    # Construir el diccionario del usuario
    nuevo_usuario = {
        "id": id_val,
        "nombre": nombre_val,
        "correo": correo_val,
        "edad": edad_val,
        "estado": estado_val,
    }

    # Guardar en la lista y registrar el ID en el set
    usuarios.append(nuevo_usuario)
    ids_registrados.add(id_val)
    
    save_data(usuarios)

    return True, Fore.GREEN +  f"Usuario '{nombre_val}' creado exitosamente."


def list_records():
    """
    Retorna una lista de strings con el resumen de cada usuario.
    """
    if not usuarios:
        return []
    
    usuarios_ordenados = sorted(usuarios, key=lambda u: u["nombre"])
    
    resumen = []
    for u in usuarios_ordenados:
        linea = f"[{u['id']}] {u['nombre']} | {u['correo']} | Edad: {u['edad']} | Estado: {u['estado']}"
        resumen.append(linea)

    return resumen

def search_record(id):
    try:
        id = int(id)
    except ValueError:
        return False, Fore.RED + "ID inválido."
    
    filtrados = [u for u in usuarios if u["id"] == id]
    
    if not filtrados:
        return False, Fore.RED + "Usuario no encontrado."
    
    u = filtrados[0]
    
    info = f"[{u['id']}] {u['nombre']} | {u['correo']} | Edad: {u['edad']} | Estado: {u['estado']}"
    return True, info

def update_record(id, nombre, correo, edad, estado):
    try:
        id = int(id)
    except ValueError:
        return False, Fore.RED + "ID inválido."
    
    if id not in ids_registrados:
        return False, Fore.RED + "Error: ID no existe."
    
    for u in usuarios:
        if u["id"] == id:

            errores = []

            ok, nombre_val = validar_nombre(nombre)
            if not ok:
                errores.append(nombre_val)

            ok, correo_val = validar_correo(correo)
            if not ok:
                errores.append(correo_val)

            ok, edad_val = validar_edad(edad)
            if not ok:
                errores.append(edad_val)

            ok, estado_val = validar_estado(estado)
            if not ok:
                errores.append(estado_val)

            if errores:
                return False, errores
            
            u["nombre"] = nombre_val
            u["correo"] = correo_val
            u["edad"] = edad_val
            u["estado"] = estado_val

            save_data(usuarios)

            return True, Fore.GREEN + "Usuario actualizado correctamente."

    return False, Fore.RED + "Error: ID no existe."

def delete_record(id):
    try:
        id = int(id)
    except ValueError:
        return False, Fore.RED + "ID inválido."
    
    global usuarios
    
    if id not in ids_registrados:
        return False, Fore.RED + "Error: ID no existe."
    
    usuarios = [u for u in usuarios if u["id"] != id]

    ids_registrados.remove(id)

    save_data(usuarios)

    return True, Fore.GREEN + "Usuario eliminado correctamente."