def print_user_options():
    options =(
        "Add vehicle to inventory",
        "Delete vehicle from inventory",
        "View current inventory",
        "Update vehicle",
        "Export current inventory",
        "Quit"
    )

    for i, option in enumerate(options, start=1):
        print(f"#{i} {option}")
    
    