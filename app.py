from flask import Flask, render_template


app = Flask(__name__)

@app.route('/index')
def index():
    titulo = "Pagina de Inicio"
    listado = ['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template('index.html', titulo=titulo, listado=listado)

@app.route('/calculos')
def calculos():
    return render_template('calculos.html')

@app.route('/distancia')
def distancia():
    return render_template('distancia.html')

@app.route('/user/<string:user>')
def user(user):
    return f"Hola, {user}"

@app.route("/numero/<int:num>")
def func(num):
    return f"El numero es: {num}"

@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1, num2):
    return f"La suma es: {num1 + num2}"

@app.route("/multi/<int:num1>/<int:num2>")
def multi(num1, num2):
    return f"La multiplicacion es: {num1 * num2}"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {} nombre: {}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")
def func1(n1, n2):
    return "La suma es: {}".format(n1+n2)

@app.route("/default")
@app.route("/default/<string:dft>")
def func2(dft="sss"):
    return "El valor por defecto es:"+ dft 

@app.route("/prueba")
def func4():
    return '''
    <html>
        <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet"
            <title>Página de prueba</title>
        </head>
        <body>
            <h1>¡Hola, esta es una página de prueba!</h1>
            <p> Esta es una pagina para probar el funcionamiento de Flask.</p>
        </body>
        <body>
    </html>
    '''

if __name__== '__main__':
    app.run(debug=True)