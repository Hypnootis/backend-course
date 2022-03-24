from flask import Flask, request, jsonify, make_response
app = Flask(__name__)

allstudents = [
    {
        "student_number": 123123,
        "name": "Alice Brown",
        "credits": 130,
        "degree": "it"
    },
    {
        "student_number": 111222,
        "name": "Bob Jones",
        "credits": 157,
        "degree": "it"
    },
    {
        "student_number": 333444,
        "name": "Richard Brown",
        "credits": 57,
        "degree": "machine"
    }
]

@app.route("/")
def hello_world():
    return "hello world"

if __name__ == "__main__":
    app.run(debug = True)