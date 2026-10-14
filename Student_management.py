
from storage import load_records



""" Search Student Using Register number"""

def search_student():

    register_number=input("Please Enter The Valid Register Number").strip()

    view_record=load_records()

    for record in view_record:
        if record["Register_Number"] == register_number:
            print(record)
            break
    else:
        print("Student Doesn't Exists")



    

    
    
