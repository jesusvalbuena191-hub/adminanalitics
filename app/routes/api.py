from flask import Blueprint, request, jsonify
from app import db
from app.models import Usuario, Rol, Permiso, RolPermiso

api_bp = Blueprint('api', __name__)

@api_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    usuario = Usuario(
        nombre_usuario=data['nombre_usuario'],
        email=data['email'],
        contrasena=data['contrasena'],
        id_rol=data['id_rol']
    )
    db.session.add(usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario creado"}), 201

@api_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([
        {
            "id_usuario": u.id_usuario,
            "nombre_usuario": u.nombre_usuario,
            "email": u.email,
            "contrasena": u.contrasena,
            "id_rol": u.id_rol
        } for u in usuarios
    ])

@api_bp.route('/roles', methods=['POST'])
def crear_rol():
    data = request.json
    rol = Rol(nombre_rol=data['nombre_rol'], descripcion=data.get('descripcion', ''))
    db.session.add(rol)
    db.session.commit()
    return jsonify({"mensaje": "Rol creado"}), 201

@api_bp.route('/permisos', methods=['POST'])
def crear_permiso():
    data = request.json
    permiso = Permiso(nombre_permiso=data['nombre_permiso'], descripcion=data.get('descripcion', ''))
    db.session.add(permiso)
    db.session.commit()
    return jsonify({"mensaje": "Permiso creado"}), 201

@api_bp.route('/rolpermisos', methods=['POST'])
def asignar_permiso_a_rol():
    data = request.json
    rp = RolPermiso(id_rol=data['id_rol'], id_permiso=data['id_permiso'])
    db.session.add(rp)
    db.session.commit()
    return jsonify({"mensaje": "Permiso asignado al rol"}), 201

@api_bp.route('/usuarios/<int:id_usuario>/permisos', methods=['GET'])
def obtener_permisos_usuario(id_usuario):
    usuario = Usuario.query.get(id_usuario)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    rol = Rol.query.get(usuario.id_rol)
    permisos = db.session.query(Permiso.nombre_permiso).join(RolPermiso).filter(RolPermiso.id_rol == rol.id_rol).all()
    lista_permisos = [p[0] for p in permisos]

    return jsonify({
        "usuario": usuario.nombre_usuario,
        "rol": rol.nombre_rol,
        "permisos": lista_permisos
    })