from fastapi import FastAPI
from uuid import uuid4

app = FastAPI()

# create a dict to store the students in memory
students = {}

# create a dict to store student data (template)
student_data = {"id": 0, "name": "", "age": 0, "email": "", "course": ""}


@app.get("/")
def home():
    return {"message": "Hello from the student api"}


# this one will get all the students
@app.get("/students")
def get_students():
    return students


# this one will get one student by their id
@app.get("/students/{student_id}")
def get_student_by_id(student_id: str):
    student = students.get(student_id)
    if not student:
        return {"error": "Student not found"}
    return student


# POST method to add a new student
@app.post("/students")
def add_student(name: str, age: int, email: str, course: str):
    new_student = student_data.copy()
    new_student["id"] = str(uuid4())
    new_student["name"] = name
    new_student["age"] = age
    new_student["email"] = email
    new_student["course"] = course

    students[new_student["id"]] = new_student
    return {"message": "Student added successfully", "data": new_student}


# Update a student
@app.put("/students/{student_id}")
def update_student(student_id: str, name: str, age: int, email: str, course: str):
    student = students.get(student_id)
    if not student:
        return {"error": "Student not found"}

    student["name"] = name
    student["age"] = age
    student["email"] = email
    student["course"] = course

    return {"message": "Student updated successfully", "data": student}


# Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    student = students.get(student_id)
    if not student:
        return {"error": "Student not found"}

    del students[student_id]

    return {"message": "Student deleted successfully"}