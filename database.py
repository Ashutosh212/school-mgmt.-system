import sqlite3

from models.main import Student, Employee

DB_FILE = "school.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def setup_database():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
        roll_number INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT,
        contact_number TEXT,
        role TEXT,
        standard TEXT,
        math INTEGER,
        physics INTEGER,
        chemistry INTEGER
    );
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS employee (
        code TEXT PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT,
        contact_number TEXT,
        role TEXT,
        subject TEXT,
        salary INTEGER,
        years_of_experience INTEGER
    );
    ''')

    conn.commit()
    conn.close()

def add_student(student: Student):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students (roll_number, name, age, gender, contact_number,
        role, standard, math, physics, chemistry)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        student.roll_number,
        student.name,
        student.age,
        student.gender,
        student.contact_number,
        student.role,
        student.standard,
        student.marks['math'],
        student.marks['physics'],
        student.marks['chemistry']
    ))
    conn.commit()
    conn.close()

    
def get_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_student_by_roll(roll_number: int) -> Student:
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE roll_number = ?", (roll_number,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return Student(
            roll_number=row[0],
            name=row[1],
            age=row[2],
            gender=row[3],
            contact_number=row[4],
            role=row[5],
            standard=row[6],
            math=row[7],
            physics=row[8],
            chemistry=row[9]
        )
    else:
        raise ValueError(f"No student found with roll number {roll_number}")

def add_employee(employee: Employee):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employee (code, name, age, gender, contact_number, role, subject, salary, years_of_experience)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        employee.code,
        employee.name,
        employee.age,
        employee.gender,
        employee.contact_number,
        employee.role,
        employee.subject,
        employee.salary,
        employee.years_of_experience
    ))
    conn.commit()
    conn.close()

def get_employee():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_employee_by_code(code: str) -> Employee:
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee WHERE code = ?", (code,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return Employee(
            code=row[0],
            name=row[1],
            age=row[2],
            gender=row[3],
            contact_number=row[4],
            role=row[5],
            subject=row[6],
            salary=row[7],
            years_of_experience=row[8]
        )
    else:
        raise ValueError(f"No employee found with code {code}")
