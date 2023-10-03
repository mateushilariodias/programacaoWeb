from flask import Flask, render_template;

app = Flask(__name__);

@app.route('/')
def index():
    return render_template('principal.html', titulo="Marketplace")

@app.route('/login')
def indexTwo():
    return render_template("<h1>Seu e-mail:</h1>", email="mateusilariodias@gmail.com")

@app.route('/clientes')
def indexThree():
    return "Aline"\
            "Julio"

app.run();