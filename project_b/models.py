from pydantic import BaseModel, Field
from typing import List

class Employee(BaseModel):
    emp_id: int
    name: str
    age: int
    teams: List[str]

class NewEmployee(BaseModel):
    emp_id: int
    name: str
    age: int= Field(gt=18,description="must be over 18")
    teams: list

