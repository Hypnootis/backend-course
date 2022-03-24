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

@app.route("/students", methods=["GET", "POST"])
def students():
    new_request = request.get_json()
    if new_request:
        

    return make_response(jsonify(allstudents), 200)

@app.route("/students/<degree>", methods=["GET"])
def degrees(degree):
    degree_students = []
    for student in allstudents:
        if student["degree"] == degree:
            degree_students.append(student)
    return make_response(jsonify(degree_students))

if __name__ == "__main__":
    app.run(debug = True)