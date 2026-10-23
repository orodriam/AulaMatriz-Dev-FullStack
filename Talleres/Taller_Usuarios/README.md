# Taller de usuarios

Proyecto en Python que procesa usuarios con filtros combinables, localiza registros mediante búsqueda binaria y verifica los resultados con pruebas unitarias. No requiere dependencias externas.

## Repositorio y entrega

Repositorio: [AulaMatriz-Dev-FullStack](https://github.com/orodriam/AulaMatriz-Dev-FullStack).

Carpeta del entregable: [Talleres/Taller_Usuarios](https://github.com/orodriam/AulaMatriz-Dev-FullStack/tree/main/Talleres/Taller_Usuarios).

Los enlaces corresponden al remoto configurado. Los cambios locales deben confirmarse y subirse a GitHub para que el entregable actualizado quede disponible. Si la rama de entrega es distinta de `main`, ajustar el enlace a la carpeta.

## Requisitos y ejecución

Python 3.10 o superior. Desde la raíz del repositorio:

```sh
cd Talleres/Taller_Usuarios
python main.py
python -m unittest discover -s test -v
```

La demostración imprime los cinco usuarios, los usuarios activos de Bogota (Ana y Lucia) y el usuario con ID 3 (Lucia). Importar `main.py` no ejecuta la demostración.

## Paso 1: procesamiento y filtros avanzados

`src/usuarios.py` contiene los datos de ejemplo y `filtrar_usuarios`. Cada registro tiene `id` (entero), `nombre` y `ciudad` (cadenas), `edad` (entero no negativo) y `activo` (booleano). Se asume que los registros cumplen este esquema.

```python
from src.usuarios import usuarios, filtrar_usuarios

resultado = filtrar_usuarios(
    usuarios,
    ciudad="  BOGOTA ",
    edad_minima=28,
    edad_maxima=42,
    activo=True,
)
assert [usuario["id"] for usuario in resultado] == [1, 3]
```

Los filtros se combinan con AND. La ciudad ignora mayúsculas y espacios exteriores; conserva las diferencias de acentos. Los límites de edad son inclusivos. `None` desactiva cada filtro y `activo=False` selecciona inactivos. Sin filtros se devuelve una lista nueva con todos los registros; sin coincidencias se devuelve `[]`.

Los parámetros con tipos incorrectos producen `TypeError`; las edades negativas y los rangos invertidos producen `ValueError`, incluso con una lista vacía. La validación de parámetros no sustituye la validación del esquema de los registros.

La implementación recorre los datos una sola vez: tiempo O(n), espacio O(k) para las k coincidencias. Conserva el orden y no modifica la entrada. La lista resultante comparte los diccionarios originales; no es una copia profunda.

## Paso 2: búsqueda binaria

`src/busqueda.py` implementa la búsqueda iterativa por ID:

```python
from src.usuarios import usuarios
from src.busqueda import busqueda_binaria

ordenados = sorted(usuarios, key=lambda usuario: usuario["id"])
assert busqueda_binaria(ordenados, 3)["nombre"] == "Lucia"
assert busqueda_binaria(ordenados, 100) is None
```

La lista debe estar ordenada ascendentemente por ID entero. La función no ordena ni comprueba el orden internamente: esa precondición permite búsquedas O(log n) con espacio adicional O(1). Con IDs repetidos devuelve la primera coincidencia de la lista; sin coincidencias o con entrada vacía devuelve `None`. No modifica los registros.

Ordenar inicialmente cuesta O(n log n) y crea una nueva lista. Para varias búsquedas sobre los mismos datos, ordenar una sola vez y reutilizarla. Si los IDs cambian, restaurar el orden antes de buscar.

## Paso 3: pruebas unitarias

La suite usa `unittest`, incluido en Python, y contiene 20 pruebas:

- Filtros individuales y combinados, inactivos y normalización de ciudad.
- Límites de edad inclusivos, entradas vacías y ausencia de coincidencias.
- Parámetros inválidos y conservación de la entrada.
- Búsqueda del primer y último usuario, listas de un elemento e IDs ausentes.
- IDs repetidos y comparación de la búsqueda binaria con una búsqueda lineal de referencia para múltiples objetivos.

Resultado esperado al ejecutar el comando de pruebas: `Ran 20 tests` y `OK`.

## Estructura

```text
Taller_Usuarios/
|-- main.py                 # Demostración de filtros y búsqueda
|-- README.md               # Instrucciones y decisiones de implementación
|-- src/
|   |-- usuarios.py         # Datos y filtros
|   `-- busqueda.py         # Búsqueda binaria
`-- test/
    |-- test_usuarios.py    # Pruebas de filtros
    `-- test_busqueda.py    # Pruebas de búsqueda
```
