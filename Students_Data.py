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

    name_validation =False
    while not name_validation:
        student_name = input("Please Enter the valid name: ").strip().lower()
        words=student_name.split()
        
        name_validation=student_name!="" and all(word.isalpha()for word in words)

    """ this code will validate the age """
    age_validation = False

    while not age_validation:
        try:
            age = int(input("Please Enter the student age : "))
        except ValueError:
            print("Please ennter age in numbers")
            continue
        if age < 18:
            print("Please enter the valid age")
        else:
            age_validation = True
           
    """ This code will check the courses we have """
    course_validation = False

    courses = [
    "MCA",
    "MBA",
    "BSC",
    "BTECH",
    "BE",
    "MCOM",
    "BCA"
]

    while not course_validation:
        course = input("Please Enter the course: ").strip().upper()

        if course in courses:
            course_validation = True
        else:
            print("Invalid Course")
    """ this will validate the duplicate register number and generate the new register number """
    next_number=1
    register_available=False
    while not register_available:
        register_available=True
        register_number=f"2026{course}{next_number:03d}"
        for student in students:
            if student["Register_Number"] == register_number:
                register_available=False
                next_number+=1
    print(f"Register Number generated Successfully and your register nuber is : {register_number}")

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