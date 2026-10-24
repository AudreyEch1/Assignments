import sqlite3

conn = sqlite3.connect("StudentRecords.db")
cursor = conn.cursor()

# remove any existing table
cursor.execute("DROP TABLE IF EXISTS StudentRecords")
cursor.execute("""
    CREATE TABLE StudentRecords (
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Age INTEGER NOT NULL,
        Major TEXT NOT NULL
    )
""")

# add 5 students with fixed values
students = [
    (1, "Alice Johnson", 20, "Biology"),
    (2, "Brian Smith", 22, "Computer Science"),
    (3, "Carla Gomez", 19, "Mathematics"),
    (4, "David Lee", 21, "History"),
    (5, "Emma Brown", 23, "Psychology"),
]
cursor.executemany(
    "INSERT INTO StudentRecords (ID, Name, Age, Major) VALUES (?, ?, ?, ?)",
    students,
)
conn.commit()

# print each student's name, age, and major
print("Students:")
cursor.execute("SELECT Name, Age, Major FROM StudentRecords")
for name, age, major in cursor.fetchall():
    print(f"  {name}, {age}, {major}")

# ask whether to add a new student
while True:
    answer = input("Do you want to add a new student? (yes/no): ").strip().lower()
    if answer in ("yes", "no"):
        break
    print("Please answer yes or no.")

if answer == "yes":
    while True:
        name = input("Enter the student's name: ").strip()
        if name:
            break
        print("Name cannot be empty.")

    while True:
        age_text = input("Enter the student's age: ").strip()
        try:
            age = int(age_text)
            break
        except ValueError:
            print("Age must be a whole number.")

    while True:
        major = input("Enter the student's major: ").strip()
        if major:
            break
        print("Major cannot be empty.")

    cursor.execute("SELECT MAX(ID) FROM StudentRecords")
    max_id = cursor.fetchone()[0]
    new_id = (max_id or 0) + 1

    cursor.execute(
        "INSERT INTO StudentRecords (ID, Name, Age, Major) VALUES (?, ?, ?, ?)",
        (new_id, name, age, major),
    )
    print(f"Added {name} to the table.")

# Commit and close
conn.commit()
conn.close()
