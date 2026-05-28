import sqlite3
def add_student():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students(name, age, course) VALUES(?,?,?)",
        (name, age, course)
    )
    conn.commit()
    conn.close()
    print("Student Added Successfully")
def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    for row in records:
        print(row)
    conn.close()
def delete_student():
    student_id = input("Enter Student ID to Delete: ")
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )
    conn.commit()
    conn.close()
    print("Student Deleted Successfully")
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("Thank You")
        break
    else:
        print("Invalid Choice")
