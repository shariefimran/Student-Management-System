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