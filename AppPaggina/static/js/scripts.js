/*!
* Start Bootstrap - Landing Page v6.0.6 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
// Obtén elementos HTML por sus ID
const leerMas = document.getElementById('leer-mas');
const contenidoAdicional = document.getElementById('contenido-adicional');

// Agrega un controlador de eventos al enlace "Leer más"
leerMas.addEventListener('click', function(e) {
  e.preventDefault(); // Evita que el enlace funcione como un enlace normal

  // Alterna la visibilidad del contenido adicional
  if (contenidoAdicional.style.display === 'none' || contenidoAdicional.style.display === '') {
    contenidoAdicional.style.display = 'block';
    leerMas.innerText = 'Leer menos'; // Opcional: cambia el texto del enlace
  } else {
    contenidoAdicional.style.display = 'none';
    leerMas.innerText = 'Leer más'; // Opcional: cambia el texto del enlace
  }
});
