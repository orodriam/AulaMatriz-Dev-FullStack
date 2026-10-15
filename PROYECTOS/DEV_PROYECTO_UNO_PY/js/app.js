const botom = document.getElementById("#btnSolicitar");
console.log(boton);
boton.addEventListener("click", function () {
    console.log("Botón clickeado");
});

const formulario = document.querySelector("formDespliegue");
formulario.addEventListener("submit", function (evento) {
    evento.preventDefault(); // Evita que el formulario se envíe de la manera tradicional
    console.log("Formulario enviado");
})

const motivo = document.querySelector("#motivo");
formulario.addEventListener("submit", function (evento) {
    evento.preventDefault(); // Evita que el formulario se envíe de la manera tradicional
    console.log("Motivo:", motivo.value);
})