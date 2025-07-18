# SchoolStack – A School Management System

> A Python-based school management platform built with **LLD principles**, **Tkinter GUI**, and **SQLite backend**, designed to manage students and employees efficiently. This project is also a base for experimenting with **LLM/ML integration** in the future.

---

## Project Overview

SchoolStack is a desktop-based school administration tool that enables basic CRUD operations (Create, Read, Update, Delete) for managing student and teacher data. It follows solid **Object-Oriented Design**, encapsulating entities such as `Person`, `Student`, and `Employee`. Data is persistently stored using **SQLite**, and the GUI is built with **Tkinter**.

---

## 🛠 Tech Stack

| Layer         | Technology        | Purpose                          |
|---------------|-------------------|----------------------------------|
| Core Logic | Python OOP        | LLD & Object-Oriented Design     |
| GUI        | Tkinter           | User Interface for operations    |
| Database    | SQLite3           | Lightweight persistent storage   |
| Packaging  | `uv`, `venv`      | Python project management        |
| (Planned)  | OpenAI / LLM APIs | Smart assistant & automation     |
| (Planned)  | Scikit-learn / XGBoost | ML models for analytics       |

---

## Key Features

- Add/Edit/Delete/View **Student** records
- Add/Edit/Delete/View **Teacher** records
- Uses **SQLite** for local data persistence
- Clean OOP structure with extensible design
- GUI forms built using Tkinter
- Proper encapsulation of classes like `Student`, `Employee`, `Person`
- Easy to extend with **service & repository layers**

---

## Skills Demonstrated

- 🔸 Low-Level Design (LLD)
- 🔸 Object-Oriented Programming (OOP)
- 🔸 GUI programming with `tkinter`
- 🔸 Database schema design (SQLite)
- 🔸 Error handling, input validation
- 🔸 Planning for ML + LLM integration

---

##  System Structure (LLD)

```text
+---------------------+
|      Person         |<-----+
+---------------------+      |
| - name              |      |
| - age               |      |
| - contact_number    |      |
+---------------------+      |
        ▲                    |
        |                    |
+---------------------+  +-------------------+
|      Student        |  |     Employee      |
+---------------------+  +-------------------+
| - standard          |  | - subject         |
| - section           |  | - salary          |
| - roll_number (PK)  |  | - emp_code (PK)   |
+---------------------+  +-------------------+
```

## Features to add:
- Get in-detailed information student/employee using LLM API
- Use Natural language to add_student/add_employee using NL2SQL model(hugging face)
- Update information about any person
- automatic schedule parent meeting if student perform lesser than average
- send fee remainder main, if fee is due