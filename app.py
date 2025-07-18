# app.py
import streamlit as st
from database import setup_database, add_student, get_students, get_student_by_roll, add_employee, get_employee, get_employee_by_code
from models.main import Student, Employee

setup_database()  

# Sidebar
page = st.sidebar.radio("Navigation", ["🏫 Add Student", "👨‍🏫 Add Teacher", "📋 View Students", "📋 View Teachers"])

# Student Form
if page == "🏫 Add Student":
    st.header("Add New Student")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=3, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    role = st.selectbox("Role", ["Student", "Teacher", "Principal", "Admin", "Accountant"])
    contact = st.text_input("Contact Number")
    standard = st.text_input("Standard")
    roll_number = st.number_input("Roll Number", step=1)

    st.subheader("Marks")
    math = st.slider("Math", 0, 100, 75)
    physics = st.slider("Physics", 0, 100, 75)
    chemistry = st.slider("Chemistry", 0, 100, 75)

    if st.button("➕ Add Student"):
        student = {
            "name": name,
            "age": age,
            "gender": gender,
            "contact_number": contact,
            "role": role,
            "standard": standard,
            "roll_number": roll_number,
            "marks": {
                "math": math,
                "physics": physics,
                "chemistry": chemistry
            }
        }
        student = Student(**student)
        add_student(student)
        st.success(f"✅ Student {name} added to DB!")

# Teacher Form
elif page == "👨‍🏫 Add Teacher":
    st.header("Add New Teacher")
    name = st.text_input("Teacher Name")
    age = st.number_input("Age", min_value=18, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    contact = st.text_input("Contact Number")
    code = st.text_input("Code")
    role = st.selectbox("Role", ["Student", "Teacher", "Principal", "Admin", "Accountant"])
    subject = st.text_input("Subject")
    salary = st.number_input("Salary", min_value=0)
    experience = st.slider("Years of Experience", 0, 40)

    if st.button("➕ Add Teacher"):
        teacher = {
            "name": name,
            "age": age,
            "gender": gender,
            "contact_number": contact,
            "code": code,
            "role": role,
            "subject": subject,
            "salary": salary,
            "years_of_experience": experience
        }
        employee = Employee(**teacher)
        add_employee(employee)
        st.success(f"✅ Teacher {name} added to DB!")

# View Students
elif page == "📋 View Students":
    st.header("📘 All Students")
    students = get_students()
    if students:
        st.dataframe(students)
    else:
        st.info("No students in the database.")

# View Teachers
elif page == "📋 View Teachers":
    st.header("📘 All Teachers")
    teachers = get_employee()
    if teachers:
        st.dataframe(teachers)
    else:
        st.info("No teachers in the database.")