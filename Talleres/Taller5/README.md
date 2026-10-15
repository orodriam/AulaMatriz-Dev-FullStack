# Implementación de Estructuras de Datos para la Gestión de Historial y Peticiones Web

## 1. Introducción

En este taller se implementaron dos estructuras de datos fundamentales: **Pila (Stack)** y **Cola (Queue)**.

Para demostrar su funcionamiento se utilizó como ejemplo un sistema web para una veterinaria.

La pila se utiliza para administrar el historial de navegación del sistema, mientras que la cola permite gestionar las peticiones de citas realizadas por los propietarios de las mascotas.

---

## 2. Caso de uso

El sistema de la veterinaria permite realizar acciones como:

- Consultar pacientes.
- Consultar citas.
- Consultar el detalle de una cita.
- Navegar hacia atrás.
- Navegar hacia adelante.
- Registrar peticiones de atención.
- Procesar peticiones según su orden de llegada.

Se implementaron las clases:

`HistorialNavegacion`

y

`ColaPeticiones`

---

## 3. Pila — HistorialNavegacion

Una pila utiliza el principio:

**LIFO — Last In, First Out**

Esto significa que el último elemento en ingresar es el primero en salir.

En el sistema de la veterinaria se utiliza para representar la navegación entre las páginas.

Ejemplo:

```text
Inicio
  ↓
Pacientes
  ↓
Citas
  ↓
Detalle de cita
```

Si el usuario se encuentra en `Detalle de cita` y presiona el botón de regresar, debe volver a `Citas`.

Para implementar correctamente las acciones de atrás y adelante se utilizaron dos pilas:

```text
Pila atrás       Página actual       Pila adelante

Inicio
Pacientes
Citas       →    Detalle de cita
```

Cuando el usuario presiona atrás, la página actual pasa a la pila de adelante y se extrae el último elemento de la pila de atrás.

---

## 4. Cola — ColaPeticiones

Una cola utiliza el principio:

**FIFO — First In, First Out**

Esto significa que el primer elemento en ingresar es el primero en salir.

En el ejemplo de la veterinaria, cada solicitud de atención se agrega al final de la cola.

Ejemplo:

```text
Entrada

Max
 ↓
Luna
 ↓
Toby
 ↓

[Max] [Luna] [Toby] → Procesamiento
```

Si Max fue registrado primero, su petición será procesada antes que las peticiones de Luna y Toby.

Para implementar esta estructura se utilizó `deque` de la biblioteca `collections` de Python.

---

## 5. Complejidad temporal

La complejidad temporal permite analizar cómo aumenta el costo de una operación cuando aumenta la cantidad de elementos almacenados.

### HistorialNavegacion

| Método | Operación principal | Complejidad |
|---|---|---:|
| `visitar()` | Agregar a pila | O(1) |
| `ir_atras()` | Extraer último elemento | O(1) |
| `ir_adelante()` | Extraer último elemento | O(1) |
| `mostrar_historial()` | Recorrer elementos | O(n) |

Las operaciones principales de una pila son eficientes porque se trabaja principalmente con el último elemento.

Agregar un elemento mediante `append()` tiene una complejidad amortizada de **O(1)**.

Extraer el último elemento utilizando `pop()` también tiene una complejidad de **O(1)**.

---

## 6. Complejidad de ColaPeticiones

| Método | Operación principal | Complejidad |
|---|---|---:|
| `agregar_peticion()` | Insertar al final | O(1) |
| `procesar_peticion()` | Extraer del inicio | O(1) |
| `mostrar_peticiones()` | Recorrer la cola | O(n) |

La estructura `deque` permite insertar elementos al final mediante `append()` y retirar elementos del inicio mediante `popleft()` de forma eficiente.

Ambas operaciones tienen una complejidad aproximada de **O(1)**.

---

## 7. ¿Por qué utilizar deque?

Una cola también podría implementarse utilizando una lista:

```python
cola = []

cola.append("Max")
cola.append("Luna")

cola.pop(0)
```

Sin embargo, eliminar el primer elemento de una lista con `pop(0)` tiene una complejidad de **O(n)**, debido a que los elementos restantes deben desplazarse.

Por esta razón se utilizó:

```python
from collections import deque
```

Con `deque` podemos utilizar:

```python
cola.append(elemento)
cola.popleft()
```

y mantener operaciones eficientes de **O(1)** en ambos extremos.

---

## 8. Prueba de rendimiento

El programa incluye una prueba sencilla utilizando `perf_counter()`.

Se realizan múltiples operaciones de inserción y extracción:

```text
100.000 inserciones
100.000 extracciones
```

La prueba se realiza tanto para la pila como para la cola.

El tiempo exacto obtenido puede variar dependiendo del computador donde se ejecute el programa.

Esta medición no reemplaza el análisis de complejidad Big O, pero permite observar experimentalmente el comportamiento de las estructuras.

---

## 9. Conclusión

La implementación permitió comprender las diferencias entre una pila y una cola mediante un ejemplo relacionado con una aplicación web de una veterinaria.

La **pila** es adecuada para manejar el historial de navegación porque utiliza el principio LIFO, donde la última página visitada puede ser la primera en recuperarse.

La **cola** es adecuada para procesar las solicitudes de los usuarios porque utiliza el principio FIFO, garantizando que las peticiones sean atendidas según su orden de llegada.

El análisis de complejidad muestra que las principales operaciones utilizadas tienen una complejidad de **O(1)**, mientras que visualizar todos los elementos requiere recorrer la estructura y presenta una complejidad de **O(n)**.