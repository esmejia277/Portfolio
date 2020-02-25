from flask import render_template, redirect, request
from flask_mail import Message
from app import mail
from app import app
from app.models import Contact, Project, db
from app.forms import ContactForm
from sqlalchemy import desc

@app.route('/', methods = ["GET", "POST"])
def index():
    form = ContactForm()

    if form.validate_on_submit():
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        reg = Contact(name = name, email = email, message = message)
        db.session.add(reg)
        db.session.commit()

        html_message = """
            <h1>New message from Portfolio!</h1>
            <h3>Contact data:</h3>
            <p>Name: {}</p>
            <p>Email: {}</p>
            <p>Message: {}</p>
        """.format(name, email, message)
        
        message_email = Message(subject="New contact",
            recipients=["estebanmejia277@gmail.com"],
            html= html_message
        )
        mail.send(message=message_email)
    
    return render_template('index.html', form=form)