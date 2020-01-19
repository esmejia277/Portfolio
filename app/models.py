from app import app
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    description = db.Column(db.Text())
    programming_language = db.Column(db.Text())
    url = db.Column(db.String(100))

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    message = db.Column(db.Text())