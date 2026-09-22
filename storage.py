import json

def save_records(students):
    """Save all student data  to a file."""

    with open("student_record.json", "w") as file:
        json.dump(students,file, indent=4)


def load_records():
    """Load student data from the file ."""

    with open("student_record.json", "r") as file:
        records = json.load(file)

    return records