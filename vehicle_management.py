from sys import exit
from typing import Tuple
from database import add_vehicle_to_db,get_database,delete_vehicle_from_db


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
        print("Vehicle added successfully.")
    elif user_input == 2:
        _id = take_user_delete_vehicle_input()
        #validate
        delete_vehicle_from_db(int(_id) - 1)
        print("Vehicle deleted successfully.")
    elif user_input == 3:
        print_inventory()
        pass


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

def take_user_delete_vehicle_input():
    return input("Enter id\n")

def print_inventory():
    print("Car details:")
    for i, car_data in enumerate(get_database(), start=1):
        print(f"#{i} {car_data[0]} {car_data[1]} {car_data[2]} {car_data[3]} {car_data[4]}")
    print()
