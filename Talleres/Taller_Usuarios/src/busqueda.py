def busqueda_binaria(lista: list[dict], objetivo: int) -> dict | None:
    """Devuelve el primer usuario con el ID objetivo, o None si no existe.

    Precondici?n: lista ordenada ascendentemente por ID entero. No se ordena
    ni se valida el orden aqu? para conservar O(log n) tiempo y O(1) espacio.
    No modifica la entrada. Si hay IDs repetidos, elige el primero.
    """
    izquierda = 0
    derecha = len(lista) - 1
    encontrado = None

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        usuario = lista[medio]

        if usuario["id"] < objetivo:
            izquierda = medio + 1
        else:
            if usuario["id"] == objetivo:
                encontrado = usuario
            derecha = medio - 1

    return encontrado
