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


""" This function will delete the student record """

def delete_student():
    register_number = input("Please enter the register number to delete the student: ").strip()

    view_delete = load_records()

    for record in view_delete:
        if record["Register_Number"] == register_number:
            print(record)
            confirmation = input("Are you sure you want to delete this student? (yes/no): ")

            if confirmation.lower() == "yes":
                view_delete.remove(record)
                print("Student Deletion Confirmed")
                save_records(view_delete)
                print("Student Record deleted Successfully")
            else:
                print("Not Deleting the student")


""" this function will filter the students"""

def filter_student():

    course=input("Please Enter the course you want to check : ")
    
    found = False
    
    for record in students:
        if record["course"]== course:
            print(record)
            found=True
    
    if found== False:  
        print("Not available")




""" this function will use for sorting the students"""

def sort_student():
    
    sort_option=input("Please Enter the choice if sorting (name or age)")

    if sort_option.lower() == "name":
        students.sort(key = lambda record : record["name"])
        print(students)
    elif sort_option.lower() == "age":
        students.sort(key=lambda record : record["age"])
        print(students)
    else:
        print("Invalid sorting choice. Please enter name or age.")





   






