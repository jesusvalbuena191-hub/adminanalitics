const listaRoles = document.getElementById("listaRoles");
const form = document.getElementById("rolForm");

form.addEventListener("submit", e => {
  e.preventDefault();
  const nuevo = {
    nombre_rol: document.getElementById("nombreRol").value,
    descripcion: document.getElementById("descripcionRol").value
  };

  fetch("/api/roles", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(nuevo)
  }).then(() => {
    form.reset();
    cargarRoles();
  });
});

function cargarRoles() {
  fetch("/api/roles")  // Si no tienes esta ruta, puedes omitir este paso
    .then(res => res.json())
    .then(data => {
      listaRoles.innerHTML = "";
      data.forEach(rol => {
        listaRoles.innerHTML += `<li class="list-group-item">${rol.nombre_rol} - ${rol.descripcion}</li>`;
      });
    });
}

cargarRoles();