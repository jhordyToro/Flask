from flask import Flask, redirect,request,make_response,render_template,session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)

class loginForm(FlaskForm):
    user_name = StringField('user name', validators=[DataRequired])
    password = PasswordField('password', validators=[DataRequired])
    submit = SubmitField('enviar')


app.config['SECRET_KEY'] = 'SUPER SECRETOxd'


todos = ['comprar huevos', 'hacer aceo', 'comprar un cepillo']

@app.errorhandler(404)
def error_not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr 
    retor = make_response(redirect('/home'))
    session['user_ip'] = user_ip

    return retor

# @app.route('/')
# def index():
#     raise(Exception('500 error'))

@app.route('/home')
def home():
    user_ip = session.get('user_ip')
    login = loginForm
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login': login
    }
    return render_template('hello.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
