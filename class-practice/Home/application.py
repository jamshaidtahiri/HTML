from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    return render_template("index.html")