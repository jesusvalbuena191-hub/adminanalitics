# app/models_registros.py
from app.models import db

# =====================================================
# MODELOS PARA LA DB SECUNDARIA (registrosmintic)
# =====================================================

class TicketPR(db.Model):
    __bind_key__ = "registrosmintic"
    __tablename__ = "pr"
    __table_args__ = {'extend_existing': True}  # 🔹 evita conflicto si la tabla ya existe

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_ticket = db.Column(db.String(50), nullable=False, unique=True)
    descripcion = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<TicketPR {self.numero_ticket}>"


class TicketIM(db.Model):
    __bind_key__ = "registrosmintic"
    __tablename__ = "im"
    __table_args__ = {'extend_existing': True}  # 🔹 recomendado también

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
    __table_args__ = {'extend_existing': True}  # 🔹 evita conflicto

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<FaseBeneficiario {self.nombre}>"
