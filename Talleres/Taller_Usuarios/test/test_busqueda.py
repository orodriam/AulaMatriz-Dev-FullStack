import unittest

from src.usuarios import usuarios
from src.busqueda import busqueda_binaria


class TestBusquedaBinaria(unittest.TestCase):

    def setUp(self):
        self.usuarios_ordenados = sorted(
            usuarios,
            key=lambda usuario: usuario["id"]
        )

    def test_usuario_existente(self):
        resultado = busqueda_binaria(
            self.usuarios_ordenados,
            3
        )

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["nombre"], "Lucia")

    def test_usuario_inexistente(self):
        resultado = busqueda_binaria(
            self.usuarios_ordenados,
            100
        )

        self.assertIsNone(resultado)

    def test_primer_usuario(self):
        resultado = busqueda_binaria(
            self.usuarios_ordenados,
            1
        )

        self.assertEqual(resultado["nombre"], "Ana")

    def test_ultimo_usuario(self):
        resultado = busqueda_binaria(
            self.usuarios_ordenados,
            5
        )

        self.assertEqual(resultado["nombre"], "Laura")

    def test_lista_vacia(self):
        self.assertIsNone(busqueda_binaria([], 1))

    def test_un_elemento(self):
        lista = [{"id": 7}]
        self.assertIs(busqueda_binaria(lista, 7), lista[0])
        self.assertIsNone(busqueda_binaria(lista, 6))

    def test_ausente_en_extremos_y_hueco(self):
        lista = [{"id": 2}, {"id": 4}, {"id": 8}]
        for objetivo in (1, 3, 9):
            with self.subTest(objetivo=objetivo):
                self.assertIsNone(busqueda_binaria(lista, objetivo))

    def test_duplicados_devuelve_primero(self):
        lista = [{"id": 2, "nombre": "Primero"}, {"id": 2}, {"id": 2}]
        self.assertIs(busqueda_binaria(lista, 2), lista[0])

    def test_coincide_con_busqueda_lineal_y_no_modifica(self):
        lista = [{"id": numero} for numero in range(0, 100, 2)]
        copia = [u.copy() for u in lista]
        for objetivo in range(-1, 102):
            with self.subTest(objetivo=objetivo):
                esperado = next((u for u in lista if u["id"] == objetivo), None)
                self.assertIs(busqueda_binaria(lista, objetivo), esperado)
        self.assertEqual(lista, copia)


if __name__ == "__main__":
    unittest.main()