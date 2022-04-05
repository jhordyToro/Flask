from imghdr import tests
from flask import Flask, flash, redirect #Es un mini framework de Python creador de APIs como FastAPI(todavia no que se diferencia tienen xd)
from flask import request #nos sirve para preguntar y obtener una respuesta del server con la ip (request Body)
from flask import make_response, url_for
from flask import render_template # puede renderizar archivos HTML para retornarlos (es obligatorio crear una carpeta con el nombre 'templates' o si no el programa no encuentra el archivo)
from flask_bootstrap import Bootstrap # es una libreria de Flask que nos permite decorar mas nuestro sitio web con su propia sintaxis
from flask import session # nos permite guardar informacion que permanece entre cada request (manda la informacion incriptada a diferencia de las cookies)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired
import unittest

from prueba import login_form 

app = Flask(__name__)
bootstrap = Bootstrap(app) # asi se inicializa BootsTrap

class log_form(FlaskForm):
    user_name = StringField('user name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('enviar')

app.config['SECRET_KEY'] = '!·$%&/()' # nos permite configurar una llave secreta 

Todos = ['TODO 1', 'TODO 2', 'TODO 3']

#CODIGOS HTTP (HTTP status)
@app.errorhandler(404) ## este decorador sirve para regresar una respuesta en caso de que nos levante el codigo 404
def not_found(error): ## esta esta acompañada del este decorador asi que preparamos una respuesta en caso de ocurra este error en ves de dejar que el propio navegador responda (no me supe explicar xd)
    return render_template('404.html', error= error) ## le decimos que archivo mandar cuando este error ocurra en mi caso yo puse un gato :)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)



#ROUTES (rutas)
@app.cli.command()
def test():
    test = unittest.TestLoader.discover('tests')
    unittest.TextTestRunner().run(tests)


# @app.route('/')
# def index():
#     raise(Exception('500 error'))

@app.route('/')
def index():
    user_ip = request.remote_addr ## aqui estamos soicitando la IP
    rediret = make_response(redirect('/home')) #estamos instanciando una variale con una respuesta (response) que redirige (redirect) a la route (/home)
    # rediret.set_cookie('user_ip', user_ip)  --> #Con esa misma variable enviamos una cookie con una key(apodo) y un valor 
    session['user_ip'] = user_ip # nos permite guardar informacionde manera segura se guarda y se manda 
    

    return rediret #posteriormente retornamos la misma (si no lo hacemos no nos redirecciona a ningun lado y por lo mismo da error por no retornar ningun valor)



@app.route('/home', methods=['GET','POST']) #por defecto flask solo tiene a get por eso hay que espesificar que estamos utilizando ya que luego conlleva a un error
def home():
    
    # user_ip = request.cookies.get('user_ip') --> #Hacemos un requeste preguntandole al server sobre la cookie que tiene nombre 'user_ip' y lo gurdamos en una variable
    user_ip = session.get('user_ip') # pedimos el valor que se guardo anteriormente y lo guardamos en otra variable (en este caso con el mismo nobre)
    login = login_form()
    user_name = session.get('username')

    context = {
        'todos': Todos,
        'user_ip': user_ip,
        'login': login,
        'username': user_name
    }
    # if request.method == 'POST': --> # tal ves no te funcione el por defecto asi que este te puede funcionar
    if login.validate_on_submit(): #si la clase login realiza un submit validator entonces:
        user_name = login.user_name.data #pedimos el dato de la llave user_name de la clase login
        session['username'] = user_name 

        flash('Your name has been successfully registered :D')

        return redirect(url_for('index'))

    return  render_template('hello.html', **context) #Un templeate -> archivo de HTML -> renderiza informacion: Estatica o DInamica -> por variables -> luego nos muestra en el navegador


