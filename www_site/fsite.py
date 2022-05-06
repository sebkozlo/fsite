from flask import Flask, render_template, template_rendered

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')