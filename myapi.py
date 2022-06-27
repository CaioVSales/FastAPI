from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
#### Dictionary
students = {
    1: {
        "name": "Caio",
        "age": "19",
        "year": "year 4"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

#### Path Parameters
@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-students/{student_id}")
def get_students(student_id: int = Path(None, description="The id of the student you want to view.")):
    return students[student_id]

##### Query parameters
@app.get("/get-by-name/{student_id}")
def get_student_(*, student_id: int, name: Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

#### Request body and Post method
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student already exists"}
    
    students[student_id] = student
    return students[student_id]