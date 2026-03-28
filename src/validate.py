# validate.py
# Módulo de validaciones para los campos de un usuario

import re
from colorama import init, Fore, Style, Back
init(autoreset=True)


def validar_id(id_usuario, ids_existentes):
    """
    Valida que el ID sea un número entero positivo y que no esté repetido.
    """
    try:
        id_usuario = int(id_usuario)
        if id_usuario <= 0:
            return False, Fore.YELLOW + "El ID debe ser un número entero positivo."
        if id_usuario in ids_existentes:
            return False, Fore.YELLOW + f"El ID {id_usuario} ya existe. Usa uno diferente."
        return True, id_usuario
    except ValueError:
        return False, Fore.YELLOW + "El ID debe ser un número entero."


def validar_nombre(nombre):
    """
    Valida que el nombre no esté vacío y solo contenga letras y espacios.
    """
    nombre = nombre.strip()
    if not nombre:
        return False, Fore.YELLOW + "El nombre no puede estar vacío."
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
        return False, Fore.YELLOW + "El nombre solo puede contener letras y espacios."
    return True, nombre


def validar_correo(correo):
    """
    Valida que el correo tenga un formato básico válido: algo@algo.algo
    """
    correo = correo.strip().lower()
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if not re.match(patron, correo):
        return False, Fore.YELLOW + "El correo no tiene un formato válido. Ejemplo: usuario@correo.com"
    return True, correo


def validar_edad(edad):
    """
    Valida que la edad sea un número entero entre 1 y 120.
    """
    try:
        edad = int(edad)
        if edad < 1 or edad > 100:
            return False, Fore.YELLOW + "La edad debe estar entre 1 y 100 años."
        return True, edad
    except ValueError:
        return False, Fore.YELLOW + "La edad debe ser un número entero."


def validar_estado(estado):
    if estado == "Activo":
        return True, estado
    else:
        return True, "Inactivo"