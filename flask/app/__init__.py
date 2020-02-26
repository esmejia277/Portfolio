from flask import Flask
from app.config import Config
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

mail = Mail(app)

from app import views