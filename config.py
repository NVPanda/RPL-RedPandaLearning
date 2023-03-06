import os

class config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'CHAVE-SECRETA-GERADA-ALEATORIAMENTE'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///pdv.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False