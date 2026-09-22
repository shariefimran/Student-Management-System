menu_item=[
    "Add Student",
    "View Students",
    "Exit"
]

def show_menu():
    """ this function will show the menu """

    print("\n =============Student Management System========")

    for index , menu in enumerate(menu_item,start=1):
        print(f"{index} . {menu}")

