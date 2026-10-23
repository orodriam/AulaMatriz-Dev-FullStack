usuarios = [
    {
        "id": 1,
        "nombre": "Ana",
        "edad": 28,
        "ciudad": "Bogota",
        "activo": True
    },
    {
        "id": 2,
        "nombre": "Carlos",
        "edad": 35,
        "ciudad": "Medellin",
        "activo": False
    },
    {
        "id": 3,
        "nombre": "Lucia",
        "edad": 42,
        "ciudad": "Bogota",
        "activo": True
    },
    {
        "id": 4,
        "nombre": "Pedro",
        "edad": 22,
        "ciudad": "Cali",
        "activo": True
    },
    {
        "id": 5,
        "nombre": "Laura",
        "edad": 31,
        "ciudad": "Bogota",
        "activo": False
    }
]


def filtrar_usuarios(
    lista: list[dict],
    ciudad: str | None = None,
    edad_minima: int | None = None,
    edad_maxima: int | None = None,
    activo: bool | None = None,
) -> list[dict]:
    """Combina filtros con AND en O(n), conservando el orden de entrada.

    Las edades son inclusivas y la ciudad ignora espacios exteriores y
    may?sculas. Devuelve una lista nueva con referencias a los usuarios.
    Los registros deben tener ciudad (str), edad (int) y activo (bool).
    """
    if ciudad is not None and not isinstance(ciudad, str):
        raise TypeError("ciudad debe ser una cadena o None")
    for nombre, edad in (("edad_minima", edad_minima), ("edad_maxima", edad_maxima)):
        if edad is not None:
            if type(edad) is not int:
                raise TypeError(f"{nombre} debe ser un entero o None")
            if edad < 0:
                raise ValueError(f"{nombre} no puede ser negativa")
    if edad_minima is not None and edad_maxima is not None:
        if edad_minima > edad_maxima:
            raise ValueError("edad_minima no puede superar edad_maxima")
    if activo is not None and type(activo) is not bool:
        raise TypeError("activo debe ser un booleano o None")

    ciudad_normalizada = ciudad.strip().casefold() if ciudad is not None else None
    return [
        usuario
        for usuario in lista
        if (ciudad_normalizada is None
            or usuario["ciudad"].strip().casefold() == ciudad_normalizada)
        and (edad_minima is None or usuario["edad"] >= edad_minima)
        and (edad_maxima is None or usuario["edad"] <= edad_maxima)
        and (activo is None or usuario["activo"] == activo)
    ]
