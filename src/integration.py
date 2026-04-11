from faker import Faker
fake = Faker("es_CO")

from file import load_data, save_data
import random

def generar_datos_falsos(**kwargs) -> tuple:
    """
    Genera usuarios falsos usando Faker y los guarda en el archivo JSON.
    """
    
    datos_existentes = load_data()
    
    cantidad = kwargs.get("cantidad", 10)
    datos_falsos = []
    
    for _ in range(cantidad):
        
        id_falso = fake.unique.random_int(min=1, max=100)
        nombre_falso = fake.name()
        correo_falso = fake.email()
        edad_falso = fake.random_int(min=18, max=80)
        estado_falso = random.choice(["Activo", "Inactivo"])    
        
        datos_falsos.append({
            "id": id_falso,
            "nombre": nombre_falso,
            "correo": correo_falso,
            "edad": edad_falso,
            "estado": estado_falso
        })
        
    datos_existentes.extend(datos_falsos)
    save_data(datos_existentes)
    return True, f"Se generaron {cantidad} usuarios falsos correctamente."