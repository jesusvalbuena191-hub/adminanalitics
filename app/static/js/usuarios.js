document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("usuarioForm");
  const tabla = document.getElementById("tablaUsuarios").querySelector("tbody");

  function cargarUsuarios() {
    fetch("/api/usuarios/")
      .then(res => res.json())
      .then(data => {
        tabla.innerHTML = "";
        data.forEach(u => {
          const row = document.createElement("tr");
          row.innerHTML = `
            <td>${u.id_usuario}</td>
            <td>${u.nombre_usuario}</td>
            <td>${u.email}</td>
            <td>${u.id_rol}</td>
            <td>
              <button class="btn btn-sm btn-primary me-2" onclick="editarUsuario(${u.id_usuario})">✏️</button>
              <button class="btn btn-sm btn-danger" onclick="eliminarUsuario(${u.id_usuario})">🗑️</button>
            </td>
          `;
          tabla.appendChild(row);
        });
      });
  }

  form.addEventListener("submit", async e => {
    e.preventDefault();
    const id = document.getElementById("id_usuario").value;
    const datos = {
      nombre_usuario: document.getElementById("nombre").value,
      email: document.getElementById("email").value,
      contrasena: document.getElementById("password").value,
      id_rol: parseInt(document.getElementById("rol").value),
    };

    const metodo = id ? "PUT" : "POST";
    const url = id ? `/api/usuarios/${id}` : "/api/usuarios";

    const res = await fetch(url, {
      method: metodo,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(datos),
    });

    if (res.ok) {
      form.reset();
      document.getElementById("id_usuario").value = "";
      cargarUsuarios();
    } else {
      alert("❌ Error al guardar usuario.");
    }
  });

  window.editarUsuario = async (id) => {
    const res = await fetch(`/api/usuarios/${id}`);
    const user = await res.json();
    document.getElementById("id_usuario").value = user.id_usuario;
    document.getElementById("nombre").value = user.nombre_usuario;
    document.getElementById("email").value = user.email;
    document.getElementById("password").value = user.contrasena;
    document.getElementById("rol").value = user.id_rol;
  };

  window.eliminarUsuario = async (id) => {
    if (confirm("¿Eliminar este usuario?")) {
      const res = await fetch(`/api/usuarios/${id}`, { method: "DELETE" });
      if (res.ok) cargarUsuarios();
      else alert("❌ Error al eliminar.");
    }
  };

  cargarUsuarios();
});