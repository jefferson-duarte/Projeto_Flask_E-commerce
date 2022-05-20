from flask import render_template, session, request, redirect, url_for, flash
from loja import app, db, bcrypt
from .forms import RegistrationForm
from .models import User
import os

@app.route('/home')
def home():
    return 'Seja bem vindo ao home da loja'

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data , username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        flash('Obrigado por registrar')
        return redirect(url_for('home'))
    return render_template('admin/registrar.html', form=form, title='Página de Registros')
