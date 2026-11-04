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
    # subjects.append(subject)
    # save_subjects(subjects)
    # print(f"{subject} added successfully")
    # return (subjects)
    subject_exists=False

    for existing_subject in subjects:
        if existing_subject['subject_code']== subject['subject_code']:
            subject_exists=True
        # print("subject code already exists please check")

        if existing_subject['subject_name']== subject['subject_name']:
            subject_exists=True
    
    if subject_exists:
        print("Subject already exists")
    else:
        subjects.append(subject)
        save_subjects(subjects)
        print("Subject added Successfully")
# add_subject()


def view_subject():

    view_subjects=load_subjects()
    if not view_subjects:
        print("there are no subjects in the db")
    else:
        for subject in view_subjects:
            print(f"{subject['subject_name'] } | {subject['subject_code']}")

# view_subject()

def update_data():
    subject_found = False
    duplicate_found = False

    admin_choice = input(
        "What do you want to edit: subject name or subject code? "
    ).strip().lower()

    if admin_choice == 'name':
        new_name = input("Please enter the new subject name: ").strip().lower()
        # existing_name=input("please enter the existing subject name: ").strip().lower()
        existing_code = input("Please enter the existing subject code: ").strip().upper()

    elif admin_choice == 'code':
        existing_code = input("Please enter the existing subject code: ").strip().upper()
        new_code = input("Please enter the new code: ").strip().upper()

    else:
        print("Invalid choice")
        return

    subjects = load_subjects()

    # Check whether the existing subject code exists
    existing_subject_found = False

    for subject in subjects:
        if subject['subject_code'] == existing_code:
            existing_subject_found = True
            break

    if not existing_subject_found:
        print("Subject code not found")
        return

    # Check for duplicate code only when updating the subject code
    if admin_choice == 'code':
        for subject in subjects:
            if (subject['subject_code'] == new_name
                    and subject['subject_code'] != existing_code):
                print("Subject code already exists")
                duplicate_found = True
                break
    
    if admin_choice == 'name':
           for subject in subjects:
               if (subject['subject_name'] == new_name
                       and subject['subject_name'] != existing_code):
                   print("Subject name already exists")
                   duplicate_found = True
                   break
       
    

    # Update the subject
    if not duplicate_found:
        for subject in subjects:
            if subject['subject_code'] == existing_code:

                if admin_choice == 'name':
                    subject['subject_name'] = new_name
                    subject_found = True

                elif admin_choice == 'code':
                    subject['subject_code'] = new_code
                    subject_found = True

                break

    if subject_found:
        save_subjects(subjects)
        print("Subject Updated Successfully")
    elif not duplicate_found:
        print("Subject code not found")
update_data()

        