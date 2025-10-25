from flask import Flask, render_template,request
import math


app = Flask(__name__)

@app.route('/index')
def index():
    titulo = "Pagina de Inicio"
    listado = ['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template('index.html', titulo=titulo, listado=listado)

@app.route('/calculos', methods=['GET', 'POST'])
def calculos():
    
    res = 0
    numero1 = 0
    numero2 = 0
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        opcion = request.form['operacion']
        if opcion == 'suma':
            res= int(numero1) + int(numero2)
        if opcion == 'resta':
            res= int(numero1) - int(numero2)
        if opcion == 'multiplicacion':
            res= int(numero1) * int(numero2)
        if opcion == 'division':
            res = numero1 / numero2 if numero2 != 0 else "Error: división por cero"

    return render_template('calculos.html', res=res, numero1=numero1, numero2=numero2)

@app.route('/distancia', methods=['GET', 'POST'])
def distancia():
    res = None
    x1 = y1 = x2 = y2 = 0

    if request.method == 'POST':
        x1 = float(request.form['x1'])
        y1 = float(request.form['y1'])
        x2 = float(request.form['x2'])
        y2 = float(request.form['y2'])
  
        dx = x2 - x1
        dy = y2 - y1
        res = math.sqrt(dx * dx + dy * dy)
 
    return render_template('distancia.html', res=res, x1=x1, y1=y1, x2=x2, y2=y2)

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