from Student_Academic import *
from storage import *
from Academic_Management import *

def add_marks():
    student_found=False
    subject_found=False

    records=load_records()
    subjects=load_subjects()
    marks_records=load_marks()

  

    register_number=input("Please Enter The Register Number : ").strip().upper()

    for record in records:
        if record['Register_Number'] == register_number:
            student_found = True
            break
    if not student_found:
        print("Student Not Found")
        return
    else:
        print("Student Found")

    subject_code=input("Please Enter the Subjcet Code : ").strip().upper()
    course=input("Please Enter the course : ").strip().lower()
    semester=int(input("please enter the semester : "))

    for subject in subjects:
        if subject['subject_code']==subject_code:
            subject_found=True
            break
    if not subject_found:
        print("Subject Not Found")
        return
    else:
        print("Subject Found")

    try:
        marks_obtained=int(input("Please Enter The Marks : "))
        if marks_obtained >= 0 and marks_obtained <=100:
            print("marks added successfully")
            marks_data={
                    "register_number":register_number,
                    "subject_code":subject_code,
                    "marks":marks_obtained,
                    "course":course,
                    "semester": semester

                }
            marks_records.append(marks_data)
            save_marks(marks_records)
        else:
            print("Marks must be between 0 and 100")
    except ValueError:
        print("Invalid Marks Please check")

    
    

# add_marks()


       
# allocate_subjects()

def allocate_subjects():
    student_found = False

    records = load_records()
    subjects = load_subjects()
    

    register_number = input("Please Enter The Register Number: ").strip().upper()

    for record in records:
        if record['Register_Number'] == register_number:
            student_course = record['course']
            student_semester = int(record['semester'])
            student_found = True
            break

    if not student_found:
        print("Student Not Found")
        return
    else:
        print("Student Found")

    view_subject()

    selected_subjects = []

    while True:
        subject_code = input(
            "Please Enter the Subject Code (or DONE): "
        ).strip().upper()

        if subject_code == "DONE":
            break

        subject_found = False

        for subject in subjects:
            if (subject['subject_code'] == subject_code
                    and subject['course'] == student_course
                    and subject['semester'] == student_semester):

                subject_found = True
                break

        if not subject_found:
            print("Subject Not Found")
            continue
        else:
            print("Subject Found")
            selected_subjects.append(subject_code)
    if not selected_subjects:
        print("No Subjects Selected")
        return
    allocation_data = {
    "register_number": register_number,
    "course": student_course,
    "semester": student_semester,
    "subject_codes": selected_subjects
}
    allocations = load_student_subjects()
    allocations_exists=False

    for allocation in allocations:
        if allocation['register_number']==register_number and allocation['semester']==student_semester:
            allocations_exists=True
            break
    if allocations_exists:
        print("Student data already exists for this semester")
    else:
        allocations.append(allocation_data)
        save_student_subjects(allocations)

# allocate_subjects()



def update_subject_allocation():
    """Add more subjects to the existing subject list."""

    existing_allocation = load_student_subjects()
    subjects = load_subjects()
    subject_found=False

    register_number = input(
        "Please Enter the Register Number: "
    ).strip().upper()

    allocation_found = False

    for allocation in existing_allocation:
        if allocation['register_number'] == register_number:
            allocation_found = True
            break

    if not allocation_found:
        print("No existing allocation")
        return
    else:
        print("Existing Allocation Found")
        print(f"Allocated subjects are: {allocation['subject_codes']}")

    existing_subjects = allocation['subject_codes']

    additional_subject = input(
        "Please enter the subject to add: "
    ).strip().upper()

    for subject in subjects:
        if subject['subject_code'] == additional_subject and subject['course'] == allocation['course'] and subject['semester'] == allocation['semester']:
            subject_found=True
            break
    if not subject_found:
        print("Invalid subject or subject does not belong to this course/semester")
    elif additional_subject in existing_subjects:
        print("Entered Subject already present")
    else:
        existing_subjects.append(additional_subject)
        save_student_subjects(existing_allocation)
        print("Subject added successfully")
            
update_subject_allocation()
    


    



