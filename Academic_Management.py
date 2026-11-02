from Student_Academic import * 


""" this function will add the subjects and subject code """


def add_subject():

    subject_name=input("Please Enter the subject name : ").strip().lower()
    subject_code=input("Please Enter the subject code : ").strip().upper()

    subject={
        "subject_name":subject_name,
        "subject_code": subject_code
    }

    subjects=load_subjects()
    subjects.append(subject)
    save_subjects(subjects)
    print(f"{subject} added successfully")
    return (subjects)

add_subject()

