from sys import exit


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
        pass
    elif user_input == 6:
        exit(0)
    else:
        raise RuntimeError(f"Unknown main menu option {user_input}")
