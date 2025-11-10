import psycopg2

# Database connection parameters
DB_CONFIG = {
    'dbname': 'assignment 3',
    'user': 'postgres',
    'password': 'newpassword',
    'host': 'localhost',
    'port': '5433'
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)

# prints current table
def getAllStudents():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students ORDER BY student_id;")
    rows = cur.fetchall()
    print("\nAll Students:")
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# adds a student
def addStudent(first_name, last_name, email, enrollment_date):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO students (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s);
    """, (first_name, last_name, email, enrollment_date))
    conn.commit()
    print(f"Added student {first_name} {last_name}.")
    cur.close()
    conn.close()

# changes a student's email by their ID
def updateStudentEmail(student_id, new_email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE students
        SET email = %s
        WHERE student_id = %s;
    """, (new_email, student_id))
    conn.commit()
    print(f"Updated student ID {student_id}'s email to {new_email}.")
    cur.close()
    conn.close()

# deletes a student by their ID
def deleteStudent(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM students WHERE student_id = %s;
    """, (student_id,))
    conn.commit()
    print(f"Deleted student ID {student_id}.")
    cur.close()
    conn.close()


if __name__ == "__main__":
    addStudent("Abraham", "Lin", "abrahamlin@cmail.carleton.ca", "2022-01-01")
    getAllStudents()
    updateStudentEmail(1, "abrahamlin@gmail.com")
    getAllStudents()
    deleteStudent(1)
    getAllStudents()

