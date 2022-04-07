from flask import Flask, request, jsonify, make_response, render_template, redirect, url_for
app = Flask(__name__, template_folder="static")

all_items = []
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
    if request.method == "POST":
        request_data = request.get_json()
        if request_data:
            allstudents.append(request_data)
            return make_response(jsonify(request_data), 200)
        else:
            return "Request must contain data in json format", 400
    else:
        return make_response(jsonify(allstudents), 200)

@app.route("/students/<degree>", methods=["GET"])
def degrees(degree):
    degree_students = []
    for student in allstudents:
        if student["degree"] == degree:
            degree_students.append(student)
    if len(degree_students) != 0:
        return make_response(jsonify(degree_students), 200)
    else:
        return "No students matching this degree"

@app.route("/students/<int:snumber>", methods=["PUT"])
def replace_student(snumber):
    student_exists = False
    request_data = request.get_json()
    for student in allstudents:
        if student["student_number"] == snumber:
            student = request_data
            student_exists = True
            return make_response({"message": "Student replaced"}, 200)

    if not student_exists:
        allstudents.append(request_data)
        return make_response({"message": "Collection created"}, 201)

@app.route("/students/<int:snumber>", methods=["PATCH"])
def update_student(snumber):
    student_exists = False
    request_data = request.get_json()
    for student in allstudents:
        if student["student_number"] == snumber:
            for key in student:
                student[key] = request_data[key]
            student_exists = True
            return make_response({"message": "Student updated"}, 200)

    if not student_exists:
        allstudents.append(request_data)
        return make_response({"message": "Student added"}, 201)

@app.route("/students/<int:snumber>", methods=["DELETE"])
def delete_student(snumber):
    deleted_student = False
    for student in allstudents:
        if student["student_number"] == snumber:
            allstudents.remove(student)
            deleted_student = True
            return make_response({"message": "Student removed"}, 200)
    if not deleted_student:
        return make_response({"message": "Student not in list"}, 400)

@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        res = request.form
        allstudents.append(res)
    return render_template("addStudentsForm.html")


@app.route("/", methods=["GET", "POST"])
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()