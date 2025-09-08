document.addEventListener("DOMContentLoaded", () => {
  const rolSelect = document.getElementById("rolSelect");
  const permisoSelect = document.getElementById("permisoSelect");
  const resultado = document.getElementById("resultado");

  fetch("/api/roles")
    .then(res => res.json())
    .then(data => {
      data.forEach(r => {
        const opt = document.createElement("option");
        opt.value = r.id_rol;
        opt.textContent = r.nombre_rol;
        rolSelect.appendChild(opt);
      });
    });

  fetch("/api/permisos")
    .then(res => res.json())
    .then(data => {
      data.forEach(p => {
        const opt = document.createElement("option");
        opt.value = p.id_permiso;
        opt.textContent = p.nombre_permiso;
        permisoSelect.appendChild(opt);
      });
    });

  document.getElementById("asignarForm").addEventListener("submit", e => {
    e.preventDefault();
    const id_rol = parseInt(rolSelect.value);
    const id_permiso = parseInt(permisoSelect.value);

    fetch("/api/rolpermisos", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id_rol, id_permiso })
    }).then(res => res.json())
      .then(data => {
        resultado.textContent = "✅ Permiso asignado correctamente.";
      });
  });
});