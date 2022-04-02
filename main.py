from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def template_test():
    
    return render_template('index.html')

# @app.route('/')
# def hello():
    
#     return render_template('template.html')
