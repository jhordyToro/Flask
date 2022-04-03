from flask import Flask, redirect #Es un mini framework de Python creador de APIs como FastAPI(todavia no que se diferencia tienen xd)
from flask import request #nos sirve para preguntar y obtener una respuesta del server con la ip (request Body)
from flask import make_response
from flask import render_template # puede renderizar archivos HTML para retornarlos (es obligatorio crear una carpeta con el nombre 'templates' o si no el programa no encuentra el archivo)

app = Flask(__name__)

Todos = ['TODO 1', 'TODO 2', 'TODO 3']

#CODIGOS HTTP (HTTP status)
@app.errorhandler(404) ## este decorador sirve para regresar una respuesta en caso de que nos levante el codigo 404
def not_found(error): ## esta esta acompañada del este decorador asi que preparamos una respuesta en caso de ocurra este error en ves de dejar que el propio navegador responda (no me supe explicar xd)
    return render_template('404.html', error= error) ## le decimos que archivo mandar cuando este error ocurra en mi caso yo puse un gato :)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)



#ROUTES (rutas)
@app.route('/')
def index():
    user_ip = request.remote_addr ## aqui estamos soicitando la IP
    rediret = make_response(redirect('/home')) #estamos instanciando una variale con una respuesta (response) que redirige (redirect) a la route (/home)
    rediret.set_cookie('user_ip', user_ip) #Con esa misma variable enviamos una cookie con una key(apodo) y un valor 

    return rediret #posteriormente retornamos la misma (si no lo hacemos no nos redirecciona a ningun lado y por lo mismo da error por no retornar ningun valor)

@app.route('/home')
def home():
    
    user_ip = request.cookies.get('user_ip') #Hacemos un requeste preguntandole al server sobre la cookie que tiene nombre 'user_ip' y lo gurdamos en una variable
    
    context = {
        'todos': Todos,
        'user_ip': user_ip
    }

    return  render_template('hello.html', **context) #Un templeate -> archivo de HTML -> renderiza informacion: Estatica o DInamica -> por variables -> luego nos muestra en el navegador



if __name__ == '__main__':
    app.run(debug=True) #esto es para hacer que el codigo corra sin hacer ningun (set FLASK_APP=main o set FLASK_DEBUG=1 y fast run) directamente lo instanciamos en el codigo