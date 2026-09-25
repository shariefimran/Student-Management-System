import json


def save_records(students):
    """Save all student data to a file."""
    with open("student_record.json", "w") as file:
        json.dump(students, file, indent=4)


def load_records():
    """Load student data from the file."""

    with open("student_record.json", "r") as file:
        records = json.load(file)

    migration_needed = False

    # Step 1: Check whether migration is required
    for record in records:
        register_number = record["Register_Number"]
        last_three = register_number[-3:]

        if not last_three.isdigit() or last_three == "000":
            migration_needed = True
            break

    # Step 2: Migrate only if required
    if migration_needed:
        course_counters = {}

        for record in records:
            course = record["course"]

            if course in course_counters:
                course_counters[course] = course_counters[course] + 1
            else:
                course_counters[course] = 1

            counter = course_counters[course]

            new_register_number = f"2026{course}{counter:03d}"

            record["Register_Number"] = new_register_number

        save_records(records)

    return records