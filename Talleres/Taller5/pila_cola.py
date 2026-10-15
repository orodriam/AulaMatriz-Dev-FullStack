from collections import deque
from time import perf_counter


# ============================================================
# PILA - HISTORIAL DE NAVEGACIÓN
# ============================================================

class HistorialNavegacion:

    def __init__(self):
        self.pila_atras = []
        self.pila_adelante = []
        self.pagina_actual = None

    def visitar(self, pagina):
        """Visita una nueva página."""

        if self.pagina_actual is not None:
            self.pila_atras.append(self.pagina_actual)

        self.pagina_actual = pagina

        # Al visitar una página nueva se elimina
        # el historial de navegación hacia adelante.
        self.pila_adelante.clear()

        print(f"Visitando: {self.pagina_actual}")

    def ir_atras(self):
        """Regresa a la página anterior."""

        if not self.pila_atras:
            print("No hay páginas anteriores.")
            return

        self.pila_adelante.append(self.pagina_actual)

        self.pagina_actual = self.pila_atras.pop()

        print(f"Regresando a: {self.pagina_actual}")

    def ir_adelante(self):
        """Avanza nuevamente a una página."""

        if not self.pila_adelante:
            print("No hay páginas siguientes.")
            return

        self.pila_atras.append(self.pagina_actual)

        self.pagina_actual = self.pila_adelante.pop()

        print(f"Avanzando a: {self.pagina_actual}")

    def mostrar_historial(self):
        """Muestra el estado actual del historial."""

        print("\n--- HISTORIAL DE NAVEGACIÓN ---")
        print("Atrás:", self.pila_atras)
        print("Página actual:", self.pagina_actual)
        print("Adelante:", self.pila_adelante)


# ============================================================
# COLA - PETICIONES DE CITAS
# ============================================================

class ColaPeticiones:

    def __init__(self):
        self.cola = deque()

    def agregar_peticion(self, propietario, mascota, motivo):
        """Agrega una petición al final de la cola."""

        peticion = {
            "propietario": propietario,
            "mascota": mascota,
            "motivo": motivo
        }

        self.cola.append(peticion)

        print(f"Petición registrada para {mascota}.")

    def procesar_peticion(self):
        """Procesa la primera petición de la cola."""

        if not self.cola:
            print("No hay peticiones pendientes.")
            return None

        peticion = self.cola.popleft()

        print(
            f"Procesando petición de {peticion['mascota']} "
            f"- Propietario: {peticion['propietario']}"
        )

        return peticion

    def mostrar_peticiones(self):
        """Muestra las peticiones pendientes."""

        print("\n--- PETICIONES PENDIENTES ---")

        if not self.cola:
            print("No hay peticiones.")
            return

        for posicion, peticion in enumerate(self.cola, start=1):

            print(
                f"{posicion}. "
                f"Mascota: {peticion['mascota']} | "
                f"Propietario: {peticion['propietario']} | "
                f"Motivo: {peticion['motivo']}"
            )


# ============================================================
# PRUEBAS
# ============================================================

print("\n================================")
print(" SISTEMA VETERINARIA HUELLITAS")
print("================================")


# ------------------------------------------------------------
# PRUEBA DE LA PILA
# ------------------------------------------------------------

print("\n=== PRUEBA HISTORIAL ===")

historial = HistorialNavegacion()

historial.visitar("Inicio")
historial.visitar("Pacientes")
historial.visitar("Citas")
historial.visitar("Detalle de cita")

historial.mostrar_historial()

print("\nUsuario presiona ATRÁS:")

historial.ir_atras()
historial.ir_atras()

historial.mostrar_historial()

print("\nUsuario presiona ADELANTE:")

historial.ir_adelante()

historial.mostrar_historial()


# ------------------------------------------------------------
# PRUEBA DE LA COLA
# ------------------------------------------------------------

print("\n=== PRUEBA COLA DE PETICIONES ===")

peticiones = ColaPeticiones()

peticiones.agregar_peticion(
    "Carlos",
    "Max",
    "Vacunación"
)

peticiones.agregar_peticion(
    "Ana",
    "Luna",
    "Consulta general"
)

peticiones.agregar_peticion(
    "Pedro",
    "Toby",
    "Dolor en una pata"
)

peticiones.agregar_peticion(
    "Laura",
    "Milo",
    "Control"
)

peticiones.mostrar_peticiones()


print("\nProcesando primera petición:")

peticiones.procesar_peticion()

peticiones.mostrar_peticiones()


# ============================================================
# PRUEBA DE RENDIMIENTO
# ============================================================

print("\n=== PRUEBA DE RENDIMIENTO ===")

cantidad = 100000


# ------------------------------------------------------------
# Rendimiento de la PILA
# ------------------------------------------------------------

pila_prueba = []

inicio = perf_counter()

for i in range(cantidad):
    pila_prueba.append(i)

for i in range(cantidad):
    pila_prueba.pop()

fin = perf_counter()

print(
    f"Pila - {cantidad} inserciones y extracciones: "
    f"{fin - inicio:.6f} segundos"
)


# ------------------------------------------------------------
# Rendimiento de la COLA
# ------------------------------------------------------------

cola_prueba = deque()

inicio = perf_counter()

for i in range(cantidad):
    cola_prueba.append(i)

for i in range(cantidad):
    cola_prueba.popleft()

fin = perf_counter()

print(
    f"Cola - {cantidad} inserciones y extracciones: "
    f"{fin - inicio:.6f} segundos"
)