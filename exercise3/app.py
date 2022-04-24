from flask import Flask, jsonify, make_response, render_template, url_for

app = Flask(__name__, template_folder="templates")

students = [
    {"student_number": 123123,
        "name": "Alice Brown",
        "credits": 130,
        "degree": "it"},
    {"student_number": 111222,
        "name": "Bob Jones",
        "credits": 157,
        "degree": "it"},
    {"student_number": 333444,
        "name": "Richard Brown",
        "credits": 57,
        "degree": "it"}
]

modify = False
modify_student = {}

@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html", my_students=students)

@app.route("/add")
def add():
    return render_template("add.html", modify=modify, student=students[modify_student])

if __name__ == "__main__":
    app.debug = True
    app.run()