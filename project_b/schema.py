# the document format that MongoDB returns is not parsable by python on its own
#  this module exists to parse the document returned by the connection into a dictionary understandable by python

# The functions below are deprecated since they only apply to single models
# def employeeEntity(item) -> dict:
#     return {
#         "id": str(item["_id"]),
#         "emp_id": item["emp_id"],
#         "name": item["name"],
#         "age": item["age"],
#         "teams": item["teams"],
#     }


# def employeesEntity(entity) -> list:
#     return [employeeEntity(item) for item in entity]

# New schema functions that apply to all models
def serializeDict(a) -> dict:
    return {
        **{i: str(a[i]) for i in a if i == "_id"},
        **{i: a[i] for i in a if i != "_id"},
    }

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]