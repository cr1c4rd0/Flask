from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.remote_addr
    reponse = make_response(redirect('/hello'))
    reponse.set_cookie('user_ip', user_ip)
    return reponse

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return render_template('hello.html', user_ip=user_ip)