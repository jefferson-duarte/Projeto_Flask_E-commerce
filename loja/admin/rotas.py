from flask import render_template, session, request, redirect, url_for
from loja import app, db

@app.route('/')
def home():
    return 'Seja bem vindo ao home da loja'

@app.route('/registrar')
def registrar():
    return render_template('admin/registrar.html', title='Registrar Usuários')