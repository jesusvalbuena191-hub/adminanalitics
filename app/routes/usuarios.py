from flask import Blueprint, jsonify, request
from app.models import Usuario, db

usuarios_bp = Blueprint('usuarios_api', __name__, url_prefix='/api/usuarios')

@usuarios_bp.route('/', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{
        'id_usuario': u.id_usuario,
        'nombre_usuario': u.nombre_usuario,
        'email': u.email,
        'contrasena': u.contrasena,
        'id_rol': u.id_rol
    } for u in usuarios])

@usuarios_bp.route('/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify({
        'id_usuario': usuario.id_usuario,
        'nombre_usuario': usuario.nombre_usuario,
        'email': usuario.email,
        'contrasena': usuario.contrasena,
        'id_rol': usuario.id_rol
    })

@usuarios_bp.route('', methods=['POST'])
def crear_usuario():
    data = request.json
    nuevo = Usuario(
        nombre_usuario=data['nombre_usuario'],
        email=data['email'],
        contrasena=data['contrasena'],
        id_rol=data['id_rol']
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario creado correctamente'}), 201

@usuarios_bp.route('/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.json
    usuario.nombre_usuario = data['nombre_usuario']
    usuario.email = data['email']
    usuario.contrasena = data['contrasena']
    usuario.id_rol = data['id_rol']
    db.session.commit()
    return jsonify({'mensaje': 'Usuario actualizado'})

@usuarios_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario eliminado'})