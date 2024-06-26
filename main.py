from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['TODO 1', 'TODO 2', 'TODO 3']

@app.route('/')
def index():
    user_ip = request.remote_addr
    reponse = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return reponse

@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos 
    }
    return render_template('hello.html', **context)

# Errors
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)