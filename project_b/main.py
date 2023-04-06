from fastapi_offline import FastAPIOffline
from models import Employee, NewEmployee
from db import conn
from schema import serializeDict, serializeList
from fastapi import Path, Query
from typing import Annotated
from pymongo import ReturnDocument

app = FastAPIOffline()


@app.get("/")
def home():
    return {"message": "Hello World!"}


@app.get("/get_all_employees")
def get_all_employees():
    # use serializeList for collections
    queryset = serializeList(conn.hrms.employee.find())
    # checking the data type of the returned queryset (it's a list)
    print(type(queryset))
    return queryset


@app.get("/get_employee/{emp_id}")
def get_employee(
    emp_id: Annotated[int, Path(title="The employee id of an employee", gt=0)]
):
    # use serializeDict for single items
    employee = serializeDict(conn.hrms.employee.find_one({"emp_id": int(emp_id)}))
    return employee


@app.get("/search_employees")
def search_employees(
    name: Annotated[str, Query(description="The name of the employee")],
    age: Annotated[int, Query(gt=18)] = None,
):
    if age == None:
        queryset = queryset = serializeList(conn.hrms.employee.find({"name": name}))
        return queryset
    queryset = serializeList(conn.hrms.employee.find({"name": name, "age": int(age)}))
    return queryset


@app.post("/add_employee")
def add_employee(employee: NewEmployee):
    conn.hrms.employee.insert_one(dict(employee))
    comment = "Employee inserted successfully"
    return {"message": comment}


@app.put("/update_employee_id/{emp_id}")
def update_employee(emp_id, employee: NewEmployee):
    conn.hrms.employee.find_one_and_update(
        {"emp_id": int(emp_id)},
        {"$set": dict(employee)},
        return_document=ReturnDocument.AFTER,
    )
