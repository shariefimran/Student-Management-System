from datetime import datetime, date

students = []

departments = {
    "MCA": "Computer Applications",
    "BCA": "Computer Applications",
    "BTECH": "Engineering",
    "BE": "Engineering",
    "MBA": "Management",
    "MCOM": "Commerce",
    "BSC": "Science"
}


def view_students():
    """This function will be used to view student data."""

    if not students:
        print("No Students Found")
    else:
        for student in students:
            print(f"Name             : {student['name']}")
            print(f"Age              : {student['age']}")
            print(f"Register Number   : {student['Register_Number']}")
            print(f"Course           : {student['course']}")
            print(f"Date of Birth    : {student['date_of_birth']}")
            print(f"Department       : {student['department']}")
            print(f"Gender           : {student['gender']}")
            print(f"Email            : {student['email']}")


def add_student():
    """Here we will add the student admission information."""

    # Validate student name
    name_validation = False

    while not name_validation:
        student_name = input(
            "Please Enter the valid name: "
        ).strip().lower()

        words = student_name.split()

        name_validation = (
            student_name != ""
            and all(word.isalpha() for word in words)
        )

    # Validate course
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
        course = input(
            "Please Enter the course: "
        ).strip().upper()

        if course in courses:
            course_validation = True
            department = departments[course]
        else:
            print("Invalid Course")

    # Generate unique register number
    next_number = 1
    register_available = False

    while not register_available:
        register_available = True

        register_number = f"2026{course}{next_number:03d}"

        for student in students:
            if student["Register_Number"] == register_number:
                register_available = False
                next_number += 1

    print(
        f"Register Number generated Successfully "
        f"and your register number is : {register_number}"
    )

    # Validate date of birth and calculate age
    dob_validation = False

    while not dob_validation:
        date_of_birth = input(
            "Please Enter The Date of birth (YYYY-MM-DD): "
        )

        try:
            today = datetime.today()

            date_of_birth = datetime.strptime(
                date_of_birth,
                "%Y-%m-%d"
            )

            age = today.year - date_of_birth.year

            if (today.month, today.day) < (
                date_of_birth.month,
                date_of_birth.day
            ):
                age = age - 1

            date_of_birth = str(date_of_birth.date())

            dob_validation = True

        except ValueError:
            print(
                "Invalid Date Format "
                "Please enter in the yyyy-mm-dd"
            )

    # Validate gender
    gender_validation = False

    genders = [
        "MALE",
        "FEMALE",
        "OTHER"
    ]

    while not gender_validation:
        gender = input(
            "Please Enter The Gender : "
        ).strip().upper()

        if gender in genders:
            gender_validation = True
        else:
            print("Invalid Gender")

    # Validate email
    email_validation = False

    while not email_validation:
        email = input(
            "Please enter the valid email: "
        ).strip().lower()

        if "@" in email:
            parts = email.split("@")

            if len(parts) == 2:
                domain_parts = parts[1].split(".")

                if (
                    parts[0] != ""
                    and domain_parts[0] != ""
                    and len(domain_parts) >= 2
                    and domain_parts[1] != ""
                    and email.count("@") == 1
                ):
                    email_validation = True
                else:
                    print("Invalid Email")
            else:
                print("Invalid Email")
        else:
            print("Invalid Email")

    # Create student record
    student = {
        "name": student_name,
        "date_of_birth": date_of_birth,
        "age": age,
        "Register_Number": register_number,
        "course": course,
        "department": department,
        "gender": gender,
        "email": email
    }

    return student