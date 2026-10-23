from src.usuarios import usuarios, filtrar_usuarios
from src.busqueda import busqueda_binaria


def main():
    print("=== TODOS LOS USUARIOS ===")

    for usuario in usuarios:
        print(usuario)


    print("\n=== USUARIOS ACTIVOS DE BOGOTA ===")

    resultado = filtrar_usuarios(
        usuarios,
        ciudad="Bogota",
        activo=True
    )

    for usuario in resultado:
        print(usuario)


    print("\n=== BUSQUEDA BINARIA ===")

    usuarios_ordenados = sorted(
        usuarios,
        key=lambda usuario: usuario["id"]
    )

    usuario_encontrado = busqueda_binaria(
        usuarios_ordenados,
        3
    )

    if usuario_encontrado:
        print("Usuario encontrado:")
        print(usuario_encontrado)
    else:
        print("Usuario no encontrado")


if __name__ == "__main__":
    main()
