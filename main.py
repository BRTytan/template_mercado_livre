from doctest import DebugRunner
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def template_test():
    home="historico"
    file = open('historico.json','r').read()
    data = json.loads(file)
    return render_template('index.html',items=data,site="Mercado - Livre fake",home=home)

@app.route('/historico')
def hello():
    file = open('historico.json','r').read()
    data = json.loads(file)
    return render_template('historico.html',items=data)

app.run(debug=True)
