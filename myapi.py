from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()
#### Dictionary
students = {
    1: {
        "name": "Caio",
        "age": "19",
        "class": "year 12"
    }
}
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