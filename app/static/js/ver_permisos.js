document.addEventListener("DOMContentLoaded", () => {
  const usuarioSelect = document.getElementById("usuarioSelect");
  const usuarioInfo = document.getElementById("usuarioInfo");
  const listaPermisos = document.getElementById("listaPermisos");

  fetch("/api/usuarios")
    .then(res => res.json())
    .then(data => {
      data.forEach(u => {
        const opt = document.createElement("option");
        opt.value = u.id_usuario;
        opt.textContent = `${u.nombre_usuario} (${u.email})`;
        usuarioSelect.appendChild(opt);
      });
    });

  document.getElementById("buscarForm").addEventListener("submit", e => {
    e.preventDefault();
    const id = usuarioSelect.value;

    fetch(`/api/usuarios/${id}/permisos`)
      .then(res => res.json())
      .then(data => {
        usuarioInfo.textContent = `Usuario: ${data.usuario} — Rol: ${data.rol}`;
        listaPermisos.innerHTML = "";
        data.permisos.forEach(p => {
          const li = document.createElement("li");
          li.className = "list-group-item";
          li.textContent = p;
          listaPermisos.appendChild(li);
        });
      });
  });
});