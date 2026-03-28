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

usuarios = []            # Lista de diccionarios: cada elemento es un usuario
ids_registrados = set()  # Set para garantizar IDs únicos


def crear_usuario(id, nombre, correo, edad, estado):
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

    return True, Fore.GREEN +  f"Usuario '{nombre_val}' creado exitosamente."


def listar_usuarios():
    """
    Retorna una lista de strings con el resumen de cada usuario.
    """
    if not usuarios:
        return []

    resumen = []
    for u in usuarios:
        linea = f"[{u['id']}] {u['nombre']} | {u['correo']} | Edad: {u['edad']} | Estado: {u['estado']}"
        resumen.append(linea)

    return resumen