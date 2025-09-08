from flask import Blueprint, jsonify
from app.models import TicketPR, TicketIM, FaseBeneficiario


reportes_bp = Blueprint("reportes", __name__)

@reportes_bp.route("/api/informes/exportar", methods=["GET"])
def exportar_informes():
    # Aquí puedes implementar la lógica para generar y devolver el reporte
    return jsonify({"mensaje": "Exportación de informes funcionando"})

# ✅ Tickets PR abiertos
@reportes_bp.route("/tickets/pr/abiertos", methods=["GET"])
def tickets_pr_abiertos():
    tickets = TicketPR.query.filter(TicketPR.fecha_cierre == None).all()
    return jsonify([{
        "id": t.id,
        "numero_ticket": t.numero_ticket,
        "departamento": t.departamento,
        "municipio": t.municipio,
        "fecha_apertura": str(t.fecha_apertura)
    } for t in tickets])


# ✅ Tickets IM cerrados
@reportes_bp.route("/tickets/im/cerrados", methods=["GET"])
def tickets_im_cerrados():
    tickets = TicketIM.query.filter(TicketIM.fecha_cierre != None).all()
    return jsonify([{
        "id": t.id,
        "numero_ticket": t.numero_ticket,
        "departamento": t.departamento,
        "fecha_cierre": str(t.fecha_cierre)
    } for t in tickets])


# ✅ Informe de beneficiarios
@reportes_bp.route("/beneficiarios", methods=["GET"])
def beneficiarios():
    beneficiarios = FaseBeneficiario.query.all()
    return jsonify([{
        "id": b.id,
        "id_beneficiario": b.id_beneficiario,
        "grupo": b.grupo,
        "dda": b.dda,
        "energia": b.energia,
        "institucion": b.institution_name
    } for b in beneficiarios])


# ✅ Consolidado (todos los reportes en una sola respuesta)
@reportes_bp.route("/consolidado", methods=["GET"])
def consolidado():
    pr_abiertos = TicketPR.query.filter(TicketPR.fecha_cierre == None).all()
    im_cerrados = TicketIM.query.filter(TicketIM.fecha_cierre != None).all()
    beneficiarios = FaseBeneficiario.query.all()

    data = {
        "tickets_pr_abiertos": [{
            "id": t.id,
            "numero_ticket": t.numero_ticket,
            "departamento": t.departamento,
            "municipio": t.municipio,
            "fecha_apertura": str(t.fecha_apertura)
        } for t in pr_abiertos],

        "tickets_im_cerrados": [{
            "id": t.id,
            "numero_ticket": t.numero_ticket,
            "departamento": t.departamento,
            "fecha_cierre": str(t.fecha_cierre)
        } for t in im_cerrados],

        "beneficiarios": [{
            "id": b.id,
            "id_beneficiario": b.id_beneficiario,
            "grupo": b.grupo,
            "dda": b.dda,
            "energia": b.energia,
            "institucion": b.institution_name
        } for b in beneficiarios]
    }

    return jsonify(data)
