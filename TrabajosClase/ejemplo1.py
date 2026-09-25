carrito = [
    {"nombre": "Teclado", "precio": 80000, "cantidad": 2},
    {"nombre": "Mouse", "precio": 40000, "cantidad": 1},
    {"nombre": "Monitor", "precio": 300000, "cantidad": 1}
]


def calcular_total(carrito, tiene_membresia):

    if len(carrito) == 0:
        return {
            "subtotal": 0,
            "descuento": 0,
            "total": 0
        }

    subtotal = 0
    unidades = 0

    for producto in carrito:
        subtotal += producto["precio"] * producto["cantidad"]
        unidades += producto["cantidad"]

    descuento = 0

    if unidades > 5:
        descuento = 0.10

    if unidades > 5 and subtotal > 200000:
        descuento = 0.15

    if tiene_membresia:
        descuento += 0.05

    if descuento > 0.25:
        descuento = 0.25

    return {
        "subtotal": subtotal,
        "descuento": descuento,
        "total": subtotal - (subtotal * descuento)
    }


print(calcular_total(carrito, True))

