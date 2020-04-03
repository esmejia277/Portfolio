from flask import render_template, redirect, request, flash
from flask_mail import Message
from app import mail
from app import app
from app.forms import ContactForm
from app.db import DatabaseConnection

import os

db = DatabaseConnection()

@app.route('/', methods = ["GET", "POST"])
def index():
    form = ContactForm()

    if form.validate_on_submit():
        name = request.form.get('name')
        country_code = request.form.get('country_code')
        telephone_number = request.form.get('telephone_number')
        email = request.form.get('email')
        message = request.form.get('message')

        sql = """ INSERT INTO Contact 
            (name, country_code, telephone_number, email, message) 
            VALUES (%s,%s,%s,%s,%s) """

        try:
            db.get_cursor().execute(sql,
                (name, country_code, telephone_number, email, message)
            )
            db.commit()
            db.close_Cursor()
            db.close_connection()
            flash("Data saved successfully")
        except Exception as error:
            print("Database Error", error)
    
        try:
            html_message = """
                <h1>New message from Portfolio!</h1>
                <h3>Contact data:</h3>
                <p>Name: {}</p>
                <p>Country code: {}</p>
                <p>Telephone number: {}</p>
                <p>Email: {}</p>
                <p>Message: {}</p>
            """.format(name, country_code, telephone_number,email, message)
        
            message_email = Message(subject="New contact",
                recipients= ["estebanmejia277@gmail.com"],
                html= html_message
            )
            mail.send(message=message_email)
            flash("Submitted data successfully")
        except Exception as error:
            print("Mail delivery error", error)

        # return render_template("success.html")
    return render_template('index.html', form=form)