from dotenv import load_dotenv
import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.abspath(os.getcwd())}/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
