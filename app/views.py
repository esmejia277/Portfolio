from flask import render_template, redirect, request
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
        data = request.form
        reg = Contact(name = data.get('name'),email = data.get('email'),
            message = data.get('message'))
        db.session.add(reg)
        db.session.commit()
        return redirect('/success')


    return render_template('public/contact.html', form = form)