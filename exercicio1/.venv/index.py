from flask import Flask, render_template, request;

app = Flask(__name__);

@app.route('/')
def index():
    return render_template('login.html', titulo="Marketplace")

@app.route('/login', methods=['POST'])
def login():
    login_user = request.form['login']
    passworld_user = request.form['passworld']

    if login_user == 'admin' and passworld_user == '123':
        return 'logou'
    else:
        return render_template('principal.html', titulo="Usuário ou senha inválido")

app.run();