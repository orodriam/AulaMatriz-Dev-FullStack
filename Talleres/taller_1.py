consultas = [
    {"mascota": "Max", "tipo": "Consulta general", "precio": 50000},
    {"mascota": "Luna", "tipo": "Vacunación", "precio": 40000},
    {"mascota": "Rocky", "tipo": "Consulta general", "precio": 50000}
]


def calcular_consultas(consultas, cliente_frecuente):

    if len(consultas) == 0:
        return {
            "subtotal": 0,
            "descuento": 0,
            "total": 0
        }

    subtotal = 0
    cantidad_consultas = 0

    for consulta in consultas:
        subtotal += consulta["precio"]
        cantidad_consultas += 1

    descuento = 0

    if cantidad_consultas > 2:
        descuento = 0.10

    if cantidad_consultas > 2 and subtotal > 100000:
        descuento = 0.15

    if cliente_frecuente:
        descuento += 0.05

    if descuento > 0.25:
        descuento = 0.25

    return {
        "subtotal": subtotal,
        "descuento": descuento,
        "total": subtotal - (subtotal * descuento)
    }


print(calcular_consultas(consultas, True))