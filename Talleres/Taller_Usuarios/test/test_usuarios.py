import unittest

from src.usuarios import usuarios, filtrar_usuarios


class TestFiltrosUsuarios(unittest.TestCase):

    def test_filtrar_por_ciudad(self):
        resultado = filtrar_usuarios(
            usuarios,
            ciudad="Bogota"
        )

        self.assertEqual(len(resultado), 3)

    def test_filtrar_activos(self):
        resultado = filtrar_usuarios(
            usuarios,
            activo=True
        )

        self.assertEqual(len(resultado), 3)

    def test_filtro_combinado(self):
        resultado = filtrar_usuarios(
            usuarios,
            ciudad="Bogota",
            activo=True
        )

        self.assertEqual(len(resultado), 2)

    def test_ciudad_inexistente(self):
        resultado = filtrar_usuarios(
            usuarios,
            ciudad="Cartagena"
        )

        self.assertEqual(resultado, [])

    def test_todos_los_filtros_y_limites_inclusivos(self):
        resultado = filtrar_usuarios(
            usuarios, ciudad="  BOGOTA ", edad_minima=28,
            edad_maxima=42, activo=True,
        )
        self.assertEqual([u["id"] for u in resultado], [1, 3])

    def test_inactivos(self):
        self.assertEqual(
            [u["id"] for u in filtrar_usuarios(usuarios, activo=False)], [2, 5]
        )

    def test_edades_por_separado(self):
        self.assertEqual(
            [u["id"] for u in filtrar_usuarios(usuarios, edad_minima=35)], [2, 3]
        )
        self.assertEqual(
            [u["id"] for u in filtrar_usuarios(usuarios, edad_maxima=28)], [1, 4]
        )

    def test_lista_vacia(self):
        self.assertEqual(filtrar_usuarios([], activo=True), [])

    def test_sin_filtros_no_modifica_entrada(self):
        copia = [u.copy() for u in usuarios]
        resultado = filtrar_usuarios(usuarios)
        self.assertEqual(resultado, copia)
        self.assertIsNot(resultado, usuarios)
        self.assertEqual(usuarios, copia)

    def test_rango_sin_coincidencias(self):
        self.assertEqual(filtrar_usuarios(usuarios, edad_minima=90), [])

    def test_parametros_invalidos(self):
        casos = [
            ({"edad_minima": -1}, ValueError),
            ({"edad_maxima": -1}, ValueError),
            ({"edad_minima": 40, "edad_maxima": 20}, ValueError),
            ({"edad_minima": True}, TypeError),
            ({"edad_maxima": "30"}, TypeError),
            ({"activo": 1}, TypeError),
            ({"ciudad": 123}, TypeError),
        ]
        for parametros, error in casos:
            with self.subTest(parametros=parametros):
                with self.assertRaises(error):
                    filtrar_usuarios(usuarios, **parametros)


if __name__ == "__main__":
    unittest.main()