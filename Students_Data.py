students = []


def view_students():
    """This function will be used to view student data."""

    if not students:
        print("No Students Found")
    else:
        for student in students:
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Register number : {student['Register_Number']}")
            print(f"Course : {student['course']}")


def add_student():
    """Here we will add the student admission information."""

    student_name = input("Please Enter the valid name: ").strip().lower()

    try:
        age = int(input("Please Enter the student age: "))
    except ValueError:
        print("Please Enter a valid age")
        return False

    course = input("Please Enter the course: ").strip().upper()

    count=0

    for student in students:
        if student['course'] == course:
            count+=1

    if age < 18:
        print("Admission Not possible for degree")
        return False
    register_number=f"2026{course}{count +1:03d}"

    print("Student data stored successfully")

    student = {
        "name": student_name,
        "age": age,
        "Register_Number":register_number,
        "course": course
    }

    return student


# while True:

#     student_data = add_student()

#     if student_data:
#         students.append(student_data)

#     choice = input("Do you want to add another student yes / no: ")

#     if choice.lower() == "no":
#         break


# view_students()