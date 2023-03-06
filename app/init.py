from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurações da aplicação
    app.config['SECRET_KEY'] = 'sua-secret-key-aqui'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pdv.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicialização de extensões
    db.init_app(app)

    # Registra blueprints
    from app.routes.sales import sales_bp
    app.register_blueprint(sales_bp)

    return app
