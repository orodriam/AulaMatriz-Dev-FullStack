usuarios = [
    {"id": 1, "nombre": "Ana", "edad": 28, "ciudad": "Bogota", "activo": True},
    {"id": 2, "nombre": "Carlos", "edad": 35, "ciudad": "Medellin", "activo": False},
    {"id": 3, "nombre": "Lucia", "edad": 42, "ciudad": "Bogota", "activo": True},
    {"id": 4, "nombre": "Pedro", "edad": 22, "ciudad": "Cali", "activo": True}
]


# Usuarios activos
activos = [u for u in usuarios if u["activo"]]


# Usuarios activos de Bogotá
bogotanos_activos = [
    u for u in usuarios
    if u["activo"] and u["ciudad"] == "Bogota"
]


# Nombres de usuarios mayores o iguales a 25 años
nombres = sorted(
    [u["nombre"] for u in usuarios if u["edad"] >= 25]
)


print(activos)
print(bogotanos_activos)
print(nombres)