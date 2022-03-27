from flask import Flask, request, jsonify, make_response, render_template
app = Flask(__name__, template_folder="src")

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
    request_data = request.get_json()
    if request_data:
        allstudents.append(request_data)
        return make_response(jsonify(request_data), 200)
    else:
        return "Request must contain data in json format", 400

@app.route("/students/<degree>", methods=["GET"])
def degrees(degree):
    degree_students = []
    for student in allstudents:
        if student["degree"] == degree:
            degree_students.append(student)
    if len(degree_students) != 0:
        return make_response(jsonify(degree_students))
    else:
        return "No students matching this degree"
@app.route("/", methods=["GET", "POST"])
def forms():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)