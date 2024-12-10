from typing import List, Tuple

db = []

def get_database() -> List:
    return db

def empty_database():
    global db
    db = []


def add_vehicle_to_db(make:str,
                      model:str,
                      year:int,
                      color:str,
                      range:float):
    
    db.append((make,model,year,color,range))


def delete_vehicle_from_db(id: int):
    db.pop(id)


def view_vehicle_from_db(id: int) -> Tuple:
    return db[id]


def update_vehicle_from_db(id: int,
                           make: str,
                           model: str,
                           year: int,
                           color: str,
                           range: float):
    db[id] = (make, model, year, color, range)



