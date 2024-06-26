from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['TODO 1', 'TODO 2', 'TODO 3']

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])  # Field for username
    password = PasswordField('Password', validators=[DataRequired()])  # Field for password
    submit = SubmitField('Submit')  # Button to submit

@app.route('/')
def index():
    user_ip = request.remote_addr
    reponse = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return reponse

@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    context = {
        'user_ip': user_ip,
        'todos': todos ,
        'login_form': login_form
    }
    return render_template('hello.html', **context)

# Errors
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)