# Student Database Management System



VIDEO LINK: https://youtu.be/uZMvWr9_9S8



### 1. Database Setup
1. Start PostgreSQL service
2. Create a database named `studentDB`
3. Run the setup script to create teh table with initial values:
        
    CREATE TABLE students(
        student_id SERIAL PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        enrollment_date DATE DEFAULT CURRENT_DATE
    );

    INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');


### Run program
    run with:
        python studentDB.py


### Features
    View all students
    Add new students
    Update student emails
    Delete students

### Usage
    Use the menu to perform CRUD operations
    Follow on-screen instructions