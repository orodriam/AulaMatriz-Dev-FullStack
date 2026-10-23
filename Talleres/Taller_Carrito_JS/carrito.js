// ======================================================
// CARRITO DE COMPRAS
// ======================================================
// Este programa simula un carrito de compras.
// Utiliza:
// - Array de objetos
// - Ciclo for
// - Condicionales if / else
// - Validaciones
// - Control de stock
// ======================================================


// ------------------------------------------------------
// 1. PRODUCTOS DEL CARRITO
// ------------------------------------------------------

const carrito = [
    {
        id: 1,
        nombre: "Teclado",
        precio: 80000,
        cantidad: 2,
        stock: 5
    },
    {
        id: 2,
        nombre: "Mouse",
        precio: 40000,
        cantidad: 1,
        stock: 10
    },
    {
        id: 3,
        nombre: "Monitor",
        precio: 600000,
        cantidad: 1,
        stock: 3
    }
];


// ------------------------------------------------------
// 2. TIPO DE CLIENTE
// ------------------------------------------------------

// Opciones:
// VIP
// Regular
// Invitado

const tipoCliente = "VIP";


// ------------------------------------------------------
// 3. FUNCIÓN PARA CALCULAR LA COMPRA
// ------------------------------------------------------

function calcularCompra(carrito, tipoCliente) {

    // Validar que el carrito exista y no esté vacío
    if (!carrito || carrito.length === 0) {
        console.log("Error: el carrito está vacío.");
        return;
    }

    // Validar que exista un tipo de cliente
    if (!tipoCliente) {
        console.log("Error: debe indicar el tipo de cliente.");
        return;
    }

    let subtotal = 0;

    console.log("=================================");
    console.log("       CARRITO DE COMPRAS");
    console.log("=================================");


    // --------------------------------------------------
    // RECORRER LOS PRODUCTOS
    // --------------------------------------------------

    for (let i = 0; i < carrito.length; i++) {

        const producto = carrito[i];

        // Validar datos básicos del producto
        if (
            !producto.nombre ||
            producto.precio <= 0 ||
            producto.cantidad <= 0
        ) {
            console.log(
                `Error: datos inválidos en el producto ${i + 1}.`
            );

            return;
        }


        // Validar disponibilidad de stock
        if (producto.cantidad > producto.stock) {

            console.log(
                `Error de stock: ${producto.nombre}`
            );

            console.log(
                `Solicitado: ${producto.cantidad}`
            );

            console.log(
                `Disponible: ${producto.stock}`
            );

            return;
        }


        // Calcular total del producto
        const totalProducto =
            producto.precio * producto.cantidad;

        subtotal += totalProducto;


        console.log(`Producto: ${producto.nombre}`);
        console.log(`Precio: $${producto.precio}`);
        console.log(`Cantidad: ${producto.cantidad}`);
        console.log(`Total producto: $${totalProducto}`);
        console.log("---------------------------------");
    }


    // --------------------------------------------------
    // CALCULAR DESCUENTO SEGÚN TIPO DE CLIENTE
    // --------------------------------------------------

    let porcentajeDescuento = 0;

    if (tipoCliente === "VIP") {

        porcentajeDescuento = 0.20;

    } else if (tipoCliente === "Regular") {

        porcentajeDescuento = 0.10;

    } else if (tipoCliente === "Invitado") {

        porcentajeDescuento = 0;

    } else {

        console.log(
            `Error: tipo de cliente "${tipoCliente}" no válido.`
        );

        return;
    }


    // --------------------------------------------------
    // CALCULAR TOTAL FINAL
    // --------------------------------------------------

    const descuento = subtotal * porcentajeDescuento;

    const total = subtotal - descuento;


    // --------------------------------------------------
    // MOSTRAR RESULTADOS
    // --------------------------------------------------

    console.log("=================================");
    console.log("       RESUMEN DE COMPRA");
    console.log("=================================");

    console.log(`Tipo de cliente: ${tipoCliente}`);
    console.log(`Subtotal: $${subtotal}`);
    console.log(
        `Descuento: ${porcentajeDescuento * 100}%`
    );
    console.log(`Valor descuento: $${descuento}`);
    console.log(`TOTAL: $${total}`);

    console.log("=================================");
}


// ------------------------------------------------------
// EJECUTAR PROGRAMA
// ------------------------------------------------------

calcularCompra(carrito, tipoCliente);