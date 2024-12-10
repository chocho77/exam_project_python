from sys import exit
from typing import Tuple
from database import add_vehicle_to_db,get_database


MAIN_MENU_OPTIONS =(
        "Add vehicle to inventory",
        "Delete vehicle from inventory",
        "View current inventory",
        "Update vehicle",
        "Export current inventory",
        "Quit"
)

def map_user_input(user_input:int):
    if user_input == 1:
        vehicle_data = take_user_add_vehicle_input()
        #validate
        add_vehicle_to_db(*vehicle_data)
        print(get_database())

    elif user_input == 6:
        exit(0)
    else:
        raise RuntimeError(f"Unknown main menu option {user_input}")

def take_user_add_vehicle_input() -> Tuple[str, str, str, str, str]:
    make = input()
    model = input()
    year = input()
    color = input()
    range = input()

    return make, model, year, color, range
