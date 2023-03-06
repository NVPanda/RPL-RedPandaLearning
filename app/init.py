from flask import Flask

app = Flask(__name__)

# Configuração do aplicativo flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pdv.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'chave-secreta'

# Importando os módulos necessários
from .routes import product, sale, customer
from .models import db

# Registro de blueprints para cada recurso
app.register_blueprint(product.bp)
app.register_blueprint(sales.bp)
app.register_blueprint(customer.bp)

# Inicialização do banco de dados
db.init_app(app)
with app.app_context():
    db.create_all()