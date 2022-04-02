from doctest import DebugRunner
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def template_test():
    
    return render_template('index.html',site="Mercado- LIvre fake")

# @app.route('/')
# def hello():
    
#     return render_template('template.html')

app.run(debug=True)