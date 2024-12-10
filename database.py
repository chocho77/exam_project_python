db = []

def add_vehicle_to_db(make:str,
                      model:str,
                      year:int,
                      color:str,
                      range:float):
    
    db.append((make,model,year,color,range))
