# Curso de Programación Full Stack

Repositorio de Óscar Iván Rodríguez Amado con ejercicios de clase, talleres y prácticas de desarrollo web en Python, JavaScript, HTML y CSS.

## Contenido

- [Estructura del repositorio](#estructura-del-repositorio)
- [Talleres](#talleres)
- [Trabajos de clase](#trabajos-de-clase)
- [Proyecto web](#proyecto-web)
- [Requisitos](#requisitos)
- [Ejecución](#ejecución)
- [Pruebas del taller de usuarios](#pruebas-del-taller-de-usuarios)

## Estructura del repositorio

```text
.
|-- .gitignore
|-- README.md
|-- Proyectos/
|   `-- DEV_PROYECTO_UNO_PY/
|       |-- index.html
|       |-- estilos.css
|       `-- js/
|           `-- app.js
|-- Talleres/
|   |-- taller_1.py
|   |-- flujo_consultas.drawio
|   |-- Taller Caso de Uso/
|   |   `-- sistema_gestion_compras_mermaid.html
|   |-- Taller5/
|   |   |-- README.md
|   |   `-- pila_cola.py
|   |-- Taller_Carrito_JS/
|   |   `-- carrito.js
|   `-- Taller_Usuarios/
|       |-- main.py
|       |-- src/
|       |   |-- usuarios.py
|       |   `-- busqueda.py
|       `-- test/
|           |-- test_usuarios.py
|           `-- test_busqueda.py
`-- TrabajosClase/
    |-- ejemplo1.py
    |-- ejemplo1.js
    |-- Ejemplo2.py
    `-- Ejemplo3.js
```

## Talleres

| Taller | Archivos | Descripción |
| --- | --- | --- |
| Consultas veterinarias | [taller_1.py](Talleres/taller_1.py) y [flujo_consultas.drawio](Talleres/flujo_consultas.drawio) | Cálculo de subtotal, descuentos y total de consultas; diagrama de flujo editable. |
| Caso de uso de compras | [sistema_gestion_compras_mermaid.html](Talleres/Taller%20Caso%20de%20Uso/sistema_gestion_compras_mermaid.html) | Documento HTML de modelado UML del sistema de gestión de compras con diagramas Mermaid. |
| Pilas y colas | [pila_cola.py](Talleres/Taller5/pila_cola.py) y [README del taller](Talleres/Taller5/README.md) | Historial de navegación con pilas, peticiones de citas con `deque` y medición de rendimiento. |
| Carrito de compras | [carrito.js](Talleres/Taller_Carrito_JS/carrito.js) | Validación de productos y stock, cálculo de subtotal y descuentos por tipo de cliente. |
| Procesamiento de usuarios | [main.py](Talleres/Taller_Usuarios/main.py), [usuarios.py](Talleres/Taller_Usuarios/src/usuarios.py) y [busqueda.py](Talleres/Taller_Usuarios/src/busqueda.py) | Filtros combinables, búsqueda binaria por ID y pruebas unitarias. |

### Carrito de compras

El programa muestra los resultados en consola y aplica descuentos del 20 % para clientes `VIP`, del 10 % para `Regular` y del 0 % para `Invitado`. Comprueba que el carrito tenga productos, que los datos básicos sean válidos y que la cantidad solicitada no supere el stock.

### Procesamiento de usuarios

El taller trabaja con cinco usuarios definidos en memoria y desarrolla tres pasos:

1. **Filtrar usuarios:** combina ciudad, edad mínima, edad máxima y estado activo mediante condiciones AND. Los límites de edad son inclusivos; la ciudad ignora mayúsculas y espacios exteriores. Valida los parámetros y recorre los registros en O(n).
2. **Buscar por ID:** utiliza búsqueda binaria sobre una lista previamente ordenada de forma ascendente. La búsqueda cuesta O(log n), devuelve la primera coincidencia si hay IDs repetidos y retorna `None` si no encuentra el objetivo. La ordenación inicial cuesta O(n log n).
3. **Verificar los resultados:** incluye 20 pruebas unitarias para filtros, parámetros inválidos, entradas vacías, límites, duplicados y conservación de los datos.

La demostración de `main.py` imprime todos los usuarios, selecciona los activos de Bogota y busca el ID 3, correspondiente a Lucia.

## Trabajos de clase

| Archivo | Contenido |
| --- | --- |
| [ejemplo1.py](TrabajosClase/ejemplo1.py) | Carrito de compras con descuentos por cantidad de unidades, subtotal y membresía. |
| [ejemplo1.js](TrabajosClase/ejemplo1.js) | Ejemplo parcial de carrito: define los productos y el retorno para un carrito vacío. |
| [Ejemplo2.py](TrabajosClase/Ejemplo2.py) | Filtrado de usuarios y ordenamiento de nombres con comprensiones de listas. |
| [Ejemplo3.js](TrabajosClase/Ejemplo3.js) | Uso de `filter`, `map` y `sort`, además de funciones de búsqueda lineal y binaria. |

## Proyecto web

La carpeta [Proyectos/DEV_PROYECTO_UNO_PY](Proyectos/DEV_PROYECTO_UNO_PY/) contiene una interfaz de solicitud de despliegue:

| Archivo | Función |
| --- | --- |
| [index.html](Proyectos/DEV_PROYECTO_UNO_PY/index.html) | Formulario para seleccionar repositorio, rama y motivo del despliegue. |
| [estilos.css](Proyectos/DEV_PROYECTO_UNO_PY/estilos.css) | Estilos de la interfaz. |
| [js/app.js](Proyectos/DEV_PROYECTO_UNO_PY/js/app.js) | Práctica de eventos del botón y del formulario. |

El proyecto contiene archivos HTML, CSS y JavaScript. El formulario declara `/api/despliegues` como destino, pero la carpeta no incluye un servidor para atender esa ruta. El script de eventos está en desarrollo y requiere corregir referencias y selectores para funcionar.

## Requisitos

- **Python 3.10 o superior** para ejecutar todos los ejercicios Python, incluido el taller de usuarios. Se utiliza la biblioteca estándar.
- **Node.js** para ejecutar los ejercicios JavaScript en la terminal.
- **Navegador web** para visualizar las páginas HTML.
- **draw.io / diagrams.net** para editar el archivo `.drawio`.
- **Conexión a internet** para cargar Mermaid desde el CDN utilizado por el documento del caso de uso.

## Ejecución

Los ejercicios son independientes. Ejecutar los siguientes comandos desde la raíz del repositorio.

### Ejercicios Python

```sh
python Talleres/taller_1.py
python Talleres/Taller5/pila_cola.py
python Talleres/Taller_Usuarios/main.py
python TrabajosClase/ejemplo1.py
python TrabajosClase/Ejemplo2.py
```

El taller de pilas y colas ejecuta demostraciones y una medición de rendimiento con 100.000 inserciones y extracciones para cada estructura. Los tiempos varían según el equipo.

### Ejercicios JavaScript

```sh
node Talleres/Taller_Carrito_JS/carrito.js
node TrabajosClase/ejemplo1.js
node TrabajosClase/Ejemplo3.js
```

`ejemplo1.js` define datos y una función parcial; su ejecución no imprime resultados. Los otros dos archivos sí muestran resultados en consola.

### Páginas HTML y diagramas

Abrir en el navegador el [formulario de despliegue](Proyectos/DEV_PROYECTO_UNO_PY/index.html) o el [documento de gestión de compras](Talleres/Taller%20Caso%20de%20Uso/sistema_gestion_compras_mermaid.html). El diagrama `Talleres/flujo_consultas.drawio` se abre con draw.io / diagrams.net.

## Pruebas del taller de usuarios

Desde la raíz del repositorio:

```sh
cd Talleres/Taller_Usuarios
python -m unittest discover -s test -v
```

| Archivo | Cantidad | Escenarios |
| --- | --- | --- |
| [test_usuarios.py](Talleres/Taller_Usuarios/test/test_usuarios.py) | 11 | Filtros individuales y combinados, edades, inactivos, parámetros inválidos y conservación de la entrada. |
| [test_busqueda.py](Talleres/Taller_Usuarios/test/test_busqueda.py) | 9 | IDs presentes y ausentes, extremos, listas vacías, un elemento, duplicados y comparación con búsqueda lineal. |

Una ejecución correcta termina con `Ran 20 tests` y `OK`. Algunos métodos verifican varios escenarios mediante `subTest`.
