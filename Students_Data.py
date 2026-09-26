
from datetime import datetime,date 

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

    """ this code will validate the date of birth """

    dob_validation=False

    while not dob_validation:
        date_of_birth=input("Please Enter The Data of birth (YYYY-MM-DD):")
        try:
              date_of_birth=datetime.strptime(date_of_birth,"%Y-%m-%d")
              date_of_birth=str(date_of_birth.date())
              dob_validation =True
        except ValueError:
            print("Invalid Date Format Please enter in the yyyy-mm-dd")
            continue

    """ this code will validate the gender"""
    gender_validation=False

    genders=[
        "MALE",
        "FEMALE",
        "OTHER"
    ]

    while not gender_validation:
        gender=input("Please Enter The Gender : ").strip().upper()

        if gender in genders:
            gender_validation =True
        else:
            print("Invalid Gender")
        


    student = {
        "name": student_name,
        "Date-Of-Birth":date_of_birth,
        "age": age,
        "Register_Number":register_number,
        "course": course,
        "gender": gender
    }

    return student


