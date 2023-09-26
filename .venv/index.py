from flask import Flask, render_template;

app = Flask(__name__);

@app.route('/')
def index():
    return render_template('aula01.html')

@app.route('/perguntaparaomundo')
def indexTwo():
    return "<h1>Como vai?</h1>" \
        "<p>Mais uma vez</p>" \
            "<img src='https://picsum.photos/200/300'>"

app.run();