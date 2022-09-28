from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello!'

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/greeting/')
@app.route('/greeting/<name>/')
def greeting(name = None):
    return render_template("greeting.html", name=name)

