from flask import Flask, request, jsonify, make_response, render_template, url_for
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
        return make_response(jsonify(degree_students), 200)
    else:
        return "No students matching this degree"

@app.route("/", methods=["GET", "POST"])
def forms():
    if request.method == "POST":
        new_item = request.form
        if new_item not in all_items:
            for key in new_item:
                if new_item[key] == "":
                    return f"Item was not added. Item must have a {key}."
                    break
                else:
                    all_items.append(new_item)
        return jsonify(all_items)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()