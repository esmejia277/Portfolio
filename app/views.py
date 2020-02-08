from flask import render_template, redirect, request
from flask_mail import Message
from app import mail
from app import app
from app.models import Contact, Project, db
from app.forms import ContactForm
from sqlalchemy import desc

@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/projects')
def projects():
    project = Project.query.order_by(Project.programming_language.desc())
    return render_template('public/projects.html', project = project)

@app.route('/about')
def about():
    return render_template('public/about.html')

@app.route('/contact', methods = ['GET', 'POST'])
def contact():

    form = ContactForm()

    if form.validate_on_submit():

        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        html_message = """
            <h1 class="bg-dark">New message from Portfolio!</h1>
            <h3>Contact data:</h3>
            <p>Name: {}</p>
            <p>Email: {}</p>
            <p>Message: {}</p>
        """.format(name, email, message)
        
        message = Message(subject="New contact",
            recipients=["estebanmejia277@gmail.com"],
            html= html_message
        )
        mail.send(message=message)

        reg = Contact(name, email, message)
        db.session.add(reg)
        db.session.commit()

        # return redirect('/success')
    return render_template('public/contact.html', form = form)