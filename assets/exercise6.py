#🧩 Ejercicio 6: Refactorizar procesamiento de ventas (separar lógica/I-O + eficiencia + pruebas)


def calculate_sale_total(sale: dict) -> float:
    """
    Calcula el total de una sola venta aplicando descuentos.
    Lanza ValueError si la venta no tiene status 'ok'.
    """
    # Si la venta no es válida se lanza una excepción antes de calcular nada
    if sale["status"] != "ok":
        raise ValueError(f"Venta inválida: {sale}")

    price = sale["price"]
    quantity = sale["quantity"] 
    discount = 0

    # Si la cantidad es mayor o igual a 10 se aplica un descuento del 10%
    if quantity >= 10:
        discount = 0.1

    # Si el cliente es vip se suma un 5% adicional al descuento ya calculado
    if sale["customer"] == "vip":
        discount = discount + 0.05

    # Se calcula el subtotal y se le aplica el descuento total acumulado
    subtotal = price * quantity
    subtotal = subtotal - (subtotal * discount)

    return subtotal


def calculate_total(sales: list) -> float:
    """
    Recorre una lista de ventas válidas y retorna la suma total.
    """
    total = 0

    # Suma el resultado de cada venta llamando a calculate_sale_total
    for sale in sales:
        total = total + calculate_sale_total(sale)

    return total


def report_invalid_sales(sales: list):
    """
    Imprime las ventas que no tienen status 'ok'.
    Esta función solo imprime, no calcula nada.
    """
    # Recorre la lista e informa únicamente las ventas que no son válidas
    for sale in sales:
        if sale["status"] != "ok":
            print("Venta inválida:", sale)


def main():
    ventas = [
        {"status": "ok",  "price": 100, "quantity": 5,  "customer": "normal"},
        {"status": "ok",  "price": 200, "quantity": 10, "customer": "vip"},
        {"status": "ok",  "price": 150, "quantity": 10, "customer": "normal"},
        {"status": "bad", "price": 50,  "quantity": 3,  "customer": "normal"},
    ]

    # Muestra las ventas inválidas antes de proceder con el cálculo
    report_invalid_sales(ventas)

    # Filtra solo las ventas válidas para evitar que calculate_total lance excepción
    ventas_validas = [s for s in ventas if s["status"] == "ok"]
    total = calculate_total(ventas_validas)
    print(f"TOTAL: {total:.2f}")


if __name__ == "__main__":
    main()