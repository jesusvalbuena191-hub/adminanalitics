document.getElementById("loginForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();

  fetch("/api/usuarios")
    .then(res => res.json())
    .then(data => {
      const user = data.find(u => u.email === email && u.contrasena === password);
      if (user) {
        localStorage.setItem("usuario", JSON.stringify(user));
        window.location.href = "/principal.html";
      } else {
        document.getElementById("mensajeError").classList.remove("d-none");
      }
    });
});