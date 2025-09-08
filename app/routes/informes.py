from flask import Blueprint, send_file
import pandas as pd
import io
from app.models_registros import TicketIM   # 👈 importar el modelo de la DB secundaria
from app.models import db

# Blueprint para los informes
informes_bp = Blueprint("informes", __name__)

@informes_bp.route("/exportar", methods=["GET"])
def exportar_informe():
    """
    Genera un archivo Excel con los datos reales de la tabla 'im' 
    en la base de datos secundaria 'registrosmintic'.
    """

    # Consulta todos los registros de la tabla 'im'
    tickets = TicketIM.query.all()

    # Convertir los datos a un DataFrame de pandas
    data = [
        {
            "fecha_apertura": t.fecha_apertura,
            "numero_ticket": t.numero_ticket,
            "canal_solicitud": t.canal_solicitud,
            "sem_id_beneficiario": t.sem_id_beneficiario,
            "departamento": t.departamento,
            "municipio": t.municipio,
            "dda": t.dda,
            "fase_instalacion": t.fase_instalacion,
            "fecha_cierre": t.fecha_cierre,
            "descripcion_apertura_o_parada": t.descripcion_apertura_o_parada,
            "estado": t.estado,
            "sem_cod_servicio": t.sem_cod_servicio,
        }
        for t in tickets
    ]

    df = pd.DataFrame(data)

    # Exportar a Excel en memoria
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Informe General")
    output.seek(0)

    return send_file(
        output,
        as_attachment=True,
        download_name="informe_general.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
