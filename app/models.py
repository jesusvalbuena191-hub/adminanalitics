from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()  # define aquí directamente


class Rol(db.Model):
    __tablename__ = 'roles'
    id_rol = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text)

class Permiso(db.Model):
    __tablename__ = 'permisos'
    id_permiso = db.Column(db.Integer, primary_key=True)
    nombre_permiso = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    contrasena = db.Column(db.String(255), nullable=False)
    id_rol = db.Column(db.Integer, db.ForeignKey('roles.id_rol'), nullable=False)
    fecha_creacion = db.Column(db.DateTime, server_default=db.func.current_timestamp())

class RolPermiso(db.Model):
    __tablename__ = 'rolpermisos'
    id_rol = db.Column(db.Integer, db.ForeignKey('roles.id_rol'), primary_key=True)
    id_permiso = db.Column(db.Integer, db.ForeignKey('permisos.id_permiso'), primary_key=True)

class Dashboard(db.Model):
    __tablename__ = 'dashboards'
    id_dashboard = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text)
    fuente_datos = db.Column(db.String(255))
    fecha_creacion = db.Column(db.DateTime, server_default=db.func.current_timestamp())



class UsuarioDashboard(db.Model):
    __tablename__ = 'usuarios_dashboards'
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), primary_key=True)
    id_dashboard = db.Column(db.Integer, db.ForeignKey('dashboards.id_dashboard'), primary_key=True)

class UsuarioReporte(db.Model):
    __tablename__ = 'usuarios_reportes'
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), primary_key=True)
    id_reporte = db.Column(db.Integer, db.ForeignKey('reportes.id_reporte'), primary_key=True)


# --- registrosmintic ---

# =====================================================
# MODELOS PARA LA DB SECUNDARIA (registrosmintic)
# =====================================================
from app.models import db


class TicketPR(db.Model):
    __bind_key__ = "registrosmintic"
    __tablename__ = "pr"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_ticket = db.Column(db.String(50), nullable=False, unique=True)
    descripcion = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<TicketPR {self.numero_ticket}>"


class TicketIM(db.Model):
    __bind_key__ = "registrosmintic"
    __tablename__ = "im"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_apertura = db.Column(db.DateTime, nullable=True)
    numero_ticket = db.Column(db.String(50), nullable=False, unique=True)
    canal_solicitud = db.Column(db.String(100), nullable=True)
    sem_id_beneficiario = db.Column(db.String(100), nullable=True)
    departamento = db.Column(db.String(100), nullable=True)
    municipio = db.Column(db.String(100), nullable=True)
    dda = db.Column(db.String(100), nullable=True)
    fase_instalacion = db.Column(db.String(100), nullable=True)
    fecha_cierre = db.Column(db.DateTime, nullable=True)
    descripcion_apertura_o_parada = db.Column(db.Text, nullable=True)
    estado = db.Column(db.String(50), nullable=True)
    sem_cod_servicio = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<TicketIM {self.numero_ticket}>"


class FaseBeneficiario(db.Model):
    __bind_key__ = "registrosmintic"
    __tablename__ = "fases_beneficiario"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<FaseBeneficiario {self.nombre}>"
