import json

import os

from colorama import init, Fore, Style, Back
init(autoreset=True)

ruta = "data/records.json"

def load_data():
    try:
        if not os.path.exists(ruta):
            return[]
        elif os.path.getsize(ruta) == 0:
            return []
        else:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return datos
    except json.JSONDecodeError:
        print(Fore.YELLOW + f"El archivo {ruta} esta dañado")
        return []
        
def save_data(data):
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
    except Exception as e:
        print(Fore.YELLOW + f"Error al guardar los datos: {e}")