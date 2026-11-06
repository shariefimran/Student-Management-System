import json


def save_subjects(subjects):
    """Save all subjects data to a file."""
    with open("Subjects.json", "w") as file:
        json.dump(subjects, file, indent=4)


def load_subjects():
    """Load student subjects data from the file."""

    with open("Subjects.json", "r") as file:
        records = json.load(file)
    return records



def save_marks(marks):
    """Save all marks data to a file."""
    with open("Marks.json", "w") as file:
        json.dump(marks, file, indent=4)


def load_marks():
    """Load student marks data from the file."""

    with open("Marks.json", "r") as file:
        records = json.load(file)

    return records


def save_student_subjects(allocations):
    """Save all marks data to a file."""
    with open("Student_Subjects.json", "w") as file:
        json.dump(allocations, file, indent=4)


def load_student_subjects():
    """Load student marks data from the file."""

    with open("Student_Subjects.json", "r") as file:
        records = json.load(file)
        return records
