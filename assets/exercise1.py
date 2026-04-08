#Ejercicio 1: Leer enteros separado por comas, calcular el promedio y manejar errores de conversión. Corrige además el cálculo lógico del promeido. 

try:
    numeros = input("Enter numbers separated by commas: ")
    lista = [int(x.strip()) for x in numeros.split(",") if x.strip() != '']
    
    if len(lista) == 0:
        print("No ingresaste números enteros.")
    else:
        promedio = sum(lista) / len(lista)
        print("El promedioe es:", promedio)    
        
except ValueError as e:
    print("Error:", e)