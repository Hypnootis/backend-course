from flask import Flask, jsonify, make_response, render_template, url_for

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run()