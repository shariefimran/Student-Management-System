from storage import *
from Students_Data import *

edit_options = {
    "1": "email",
    "2": "phone",
    "3": "adress",
    "4": "course",
    "5": "Exit"
}


"""Search Student Using Register Number"""

def search_student(students=None):
    register_number = input("Please Enter The Valid Register Number: ").strip()

    if students is None:
        students = load_records()

    for record in students:
        if record["Register_Number"] == register_number:
            return record

    return None


"""Update Student Record Based On User Input"""

def edit_student():
    for items, options in edit_options.items():
        print(items, options)

    user_choice = input("Please Enter The Choice: ").strip()

    if user_choice not in edit_options:
        print("Invalid Choice. Please enter a valid choice.")
        return

    if user_choice == "5":
        print("Exiting Update Student Menu.")
        return

    students = load_records()
    student_record = search_student(students)

    if student_record is None:
        print("Student doesn't exist.")
        return

    print(student_record)

    selected_field = edit_options[user_choice]
    new_value = input(f"Enter the new {selected_field}: ").strip()

    student_record[selected_field] = new_value

    save_records(students)

    print("Student record updated successfully!")