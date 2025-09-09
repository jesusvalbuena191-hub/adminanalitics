from flask import Flask
from app.models import db   # 👈 importa db desde models
from app.routes.usuarios import usuarios_bp
from app.routes.informes import informes_bp

def create_app():
    app = Flask(__name__)

    # Base principal
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/adminanalyticsdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 🔗 Otras bases con bind_key
    app.config['SQLALCHEMY_BINDS'] = {
        "registrosmintic": "mysql+pymysql://root:@localhost/registrosmintic"
    }

    db.init_app(app)

    # registrar blueprints
    app.register_blueprint(usuarios_bp, url_prefix="/api/usuarios")
    app.register_blueprint(informes_bp, url_prefix="/api/informes")

    with app.app_context():
        db.create_all()  # crea tablas en todas las bases según __bind_key__

    return app
