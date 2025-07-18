class Person:
    def __init__(self, name, age, gender, contact_number, role:str):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_number = contact_number
        self.role = role

    def __str__(self):
        return f"Name: {self.name}, Role: {self.role}"
    
class Employee(Person):
    def __init__(self, name: str, age: int, gender: str, contact_number: int, role: str, code: str, subject: str, salary: int, years_of_experience: int):
        super().__init__(name, age, gender, contact_number, role)
        self.subject = subject
        self.salary = salary
        self.years_of_experience = years_of_experience
        self.code = code
    
class Student(Person):
    def __init__(self, name: str, age: int, gender: str, contact_number: int, role: str, standard: str, roll_number: int, marks: dict):
        super().__init__(name, age, gender, contact_number, role)
        self.standard = standard
        self.roll_number = roll_number
        self.marks = marks

def main():
    emp = Employee("Rubina", 30, "Female", "16515184", "Teacher", "SSR", "Social Science", 20000, 3)
    print(emp)

if __name__ == "__main__":
    main()
