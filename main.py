from menu import show_menu

from Students_Data import add_student,view_students,students
from storage import save_records,load_records

def main():
    records=load_records()
    students.extend(records)
    while True:
        show_menu()
        choice=input("Enter your choice : ")
        if choice =="1":
            student_data=add_student()

            if student_data:
                students.append(student_data)
                save_records(students)
                
        elif choice == "2":
            view_students()
        elif choice =="3":
            print("Good Bye")
            break
            
        else:
            print("Invalid Choice")

        



if __name__ == "__main__":
    main()