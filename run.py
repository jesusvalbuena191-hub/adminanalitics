from flask import Flask, render_template
from app import create_app, db

app = create_app()

# Pantallas frontend
@app.route('/')
def login_page():
    return render_template("login.html")

@app.route('/dashboard.html')
def dashboard_page():
    return render_template("dashboard.html")

@app.route('/usuarios.html')
def usuarios_page():
    return render_template("usuarios.html")

@app.route('/roles.html')
def roles_page():
    return render_template("roles.html")

@app.route('/permisos.html')
def permisos_page():
    return render_template("permisos.html")

@app.route('/asignar_permisos.html')
def asignar_permisos_page():
    return render_template("asignar_permisos.html")

@app.route('/ver_permisos.html')
def ver_permisos_page():
    return render_template("ver_permisos.html")
@app.route('/principal.html')
def principal_page():
    return render_template("principal.html")

@app.route('/informes.html')
def informes_page():
    return render_template("informes.html")



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)