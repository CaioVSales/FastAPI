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

class updateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

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

#### Put method
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: updateStudent):
    if student_id not in students:
        return {"Error": "Student not found"}
    
    if student.name != None:
        students[student_id].name = student.name
        
    if student.age != None:
        students[student_id].age = student.age
    
    if student.year != None:
        students[student_id].year = student.year
        
    return students[student_id]

#### Delete Method
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    del students[student_id]
    return {"Message": "Student deleted successfully"}