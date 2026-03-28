# Ejercicio 4: Analiza el siguiente “código existente” y realiza un -> refactor <-, tener en cuenta los problemas que se plantean al final.

# Código original (difícil de mantener)

op =  input("Ingrese operación (suma, resta, multi, divi): ")
a = int(input("Ingrese primer número: "))
b = int(input("Ingrese segundo número: "))

def calc(a, b, op):
    
    # match op:
    #     case "suma":
    #         return a + b
    #     case "resta":
    #         return a - b
    #     case "multi":
    #         return a * b
    #     case "divi":
    #         if b == 0:
    #             return "error"
    #         return a / b
    #     case _:
    #         return None
    
        ops = {
            "suma": lambda x, y: x + y,
            "resta": lambda x, y: x - y,
            "multi": lambda x, y: x * y,
            "divi": lambda x, y: "error" if y == 0 else x / y        
        }
        
        func = ops.get(op)
        return func(a, b) if func else None

result = calc(a, b, op)
print("El resultado de", op, "es:", result)