const listaPermisos = document.getElementById("listaPermisos");
const form = document.getElementById("permisoForm");

form.addEventListener("submit", e => {
  e.preventDefault();
  const nuevo = {
    nombre_permiso: document.getElementById("nombrePermiso").value,
    descripcion: document.getElementById("descripcionPermiso").value
  };

  fetch("/api/permisos", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(nuevo)
  }).then(() => {
    form.reset();
    cargarPermisos();
  });
});

function cargarPermisos() {
  fetch("/api/permisos") // Si no tienes esta ruta, puedes omitir este paso
    .then(res => res.json())
    .then(data => {
      listaPermisos.innerHTML = "";
      data.forEach(p => {
        listaPermisos.innerHTML += `<li class="list-group-item">${p.nombre_permiso}</li>`;
      });
    });
}

cargarPermisos();