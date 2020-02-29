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
        country_code = request.form.get('country_code')
        telephone_number = request.form.get('telephone_number')
        message = request.form.get('message')

        # reg = Contact(
        #     name = name,
        #     country_code = country_code,
        #     telephone_number = telephone_number, 
        #     email = email,
        #     message = message
        # )
        # db.session.add(reg)
        # db.session.commit()

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
            recipients=["estebanmejia277@gmail.com"],
            html= html_message
        )
        mail.send(message=message_email)
        return render_template("success.html")
    return render_template('index.html', form=form)