const usuarios = [
    { id: 1, nombre: "Ana", edad: 28, ciudad: "Bogota", activo: true },
    { id: 2, nombre: "Carlos", edad: 35, ciudad: "Medellin", activo: false },
    { id: 3, nombre: "Lucia", edad: 42, ciudad: "Bogota", activo: true },
    { id: 4, nombre: "Pedro", edad: 22, ciudad: "Cali", activo: true }
];

const activos = usuarios.filter(u => u.activo);

const bogotanosActivos = usuarios.filter(
    u => u.activo && u.ciudad === "Bogota"
);

const nombres = usuarios
    .filter(u => u.edad >= 25)
    .map(u => u.nombre)
    .sort();

function busquedaLineal(lista, objetivo) {
    for (let i = 0; i < lista.length; i++) {
        if (lista[i] === objetivo) return i;
    }
    return -1;
}

function busquedaBinaria(lista, objetivo) {
    let inicio = 0;
    let fin = lista.length - 1;

    while (inicio <= fin) {
        const medio = Math.floor((inicio + fin) / 2);
        if (lista[medio] === objetivo) return medio;
        if (lista[medio] < objetivo) inicio = medio + 1;
        else fin = medio - 1;
    }
    return -1;
}


console.log(activos);
console.log(bogotanosActivos);
console.log(nombres);