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

    # Step 1: Check and migrate register numbers
    register_migration_needed = False

    for record in records:
        register_number = record["Register_Number"]
        last_three = register_number[-3:]

        if not last_three.isdigit() or last_three == "000":
            register_migration_needed = True
            break

    if register_migration_needed:
        course_counters = {}

        for record in records:
            course = record["course"]

            if course in course_counters:
                course_counters[course] += 1
            else:
                course_counters[course] = 1

            counter = course_counters[course]

            new_register_number = f"2026{course}{counter:03d}"

            record["Register_Number"] = new_register_number

        migration_needed = True

    # Step 2: Migrate Date of Birth
    for record in records:

        if "date_of_birth" not in record:

            if "Date-Of-Birth" in record:
                record["date_of_birth"] = record["Date-Of-Birth"]
                del record["Date-Of-Birth"]

            else:
                record["date_of_birth"] = "N/A"

            migration_needed = True

    # Step 3: Save only if migration was required
    if migration_needed:
        save_records(records)

    return records