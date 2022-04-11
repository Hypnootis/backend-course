from flask import Flask, jsonify, make_response, render_template, url_for

app = Flask(__name__, template_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello/<user>")
def hello(user):
    return render_template("hello.html", username = user)

if __name__ == "__main__":
    app.debug = True
    app.run()