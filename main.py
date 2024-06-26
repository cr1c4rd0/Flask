from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

todos = ['TODO 1', 'TODO 2', 'TODO 3']

@app.route('/')
def index():
    user_ip = request.remote_addr
    reponse = make_response(redirect('/hello'))
    reponse.set_cookie('user_ip', user_ip)
    return reponse

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos 
    }
    return render_template('hello.html', **context)

# Errors
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)