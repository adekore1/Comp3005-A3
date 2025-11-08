# Install libraries so the db works
import psycopg2
from psycopg2 import sql
from datetime import datetime

class studentDB:
    # Implementation that Handles all database operations for the students table
    """
    This class provides methods to connect to PostgreSQL and perform
    CRUD operations on student records including:
    - Retrieving all students
    - Adding new students
    - Updating student emails
    - Deleting student records
    """


    # Initialize database connection parameters with default values.
    def __init__(self, dbname="studentDB", user="postgres", password="101316017", host='localhost', port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host    
        self.port = port
        self.connection = None

    # Connect to the database 
    # Returns:
        # bool: True if connection successful, False otherwise
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Database connected successfully")
            return True
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return False


    # disconnect from the database safely
    def disconnect(self):
        # Checks if connection exists before attempting to close it
        if self.connection:
            self.connection.close()
            print("Database connection closed")


    # ===================================================

    def getAllStudents(self):
        # Retrieve and display all student records from the database
        """Executes SELECT query to fetch all students ordered by student_id.
        Formats and displays results in a readable table format.
        Handles cases where no connection exists or query fails."""

        # check if connection exists
        if not self.connection:
            self.connect()

        try:
        # Create a cursor object to execute SQL queries
            cursor = self.connection.cursor()

            # Execute the SELECT query to fetch all students
            cursor.execute("SELECT * FROM students;")

            # Fetch all results from the executed query
            students = cursor.fetchall()

            # Display the student records in a formatted table
            print("-" *75)
            print(f"{'ID':<4} {'First Name':<15} {'Last Name':<15} {'Email':<25} {'Enrollment Date'}")
            print("-" *75)
            for student in students:
                print(f"{student[0]:<4} {student[1]: <15} {student[2]: <15} {student[3]: <25} {student[4]} ")

            cursor.close()
        
        except Exception as e:
            print(f"Error fetching students: {e}")


    # ===================================================

    def addStudent(self, first_name, last_name, email, enrollment_date):
        # Add a new student record to the database


        # Check if connection exists
        if not self.connection:
            self.connect()

        try:
            cursor = self.connection.cursor()

            #  Prepare the INSERT query
            insert_query_text = """
                                INSERT INTO students (first_name, last_name, email, enrollment_date)
                                VALUES (%s, %s, %s, %s)
                                """
            
            cursor.execute(insert_query_text, (first_name, last_name, email, enrollment_date))

            # Commit the transaction (save changes to the database)
            self.connection.commit()
            print("Student added successfully")

            cursor.close()


        except Exception as e:
            print(f"Error adding student: {e}")
    

    # ===================================================

    def updateStudentEmail(self, student_id, new_email):
        # Update the email of an existing student record

        # Check if connection exists
        if not self.connection:
            self.connect()

        try:
            # Create a cursor object to execute SQL queries
            cursor = self.connection.cursor()

            # Prepare the UPDATE query
            update_query_text = """
                            UPDATE students
                            SET email = %s
                            WHERE student_id = %s
                            """
            
            # Execute the UPDATE query with provided parameters
            cursor.execute(update_query_text, (new_email, student_id))

            # Commit the transaction to save changes
            self.connection.commit()

            print("Student email updated successfully")

            cursor.close()


        except Exception as e:
            print(f"Error updating student email: {e}")


    # ==================================================

    def deleteStudent(self, student_id):
        # Delete a student record from the database

        # Check if connection exists
        if not self.connection:
            self.connect()
        
        try:

            cursor = self.connection.cursor()

            # Prepare the DELETE query
            delete_query_text = """
                            DELETE FROM students
                            WHERE student_id = %s
                            """
            
            # Execute the DELETE query with provided student_id
            cursor.execute(delete_query_text, (student_id,))

            self.connection.commit()

            print("Student deleted successfully")

            cursor.close()
        
        except Exception as e:
            print(f"Error deleting student: {e}")


# ==============================================================================================





def main():
    # Main function to run the student database management system
    """Provides a console-based menu system for interacting with the
    student database. Handles user input, menu navigation, and
    coordinates calls to appropriate database operations."""

    print("Student Database Management System")
    print("-" *40)

# Create an instance of the studentDB class
    db = studentDB()

    # Attempt to connect to the database
    if db.connect():
        try:

            # Display menu and handle user choices
            while True:
                print("\nMenu:")
                print("1. View All Students")
                print("2. Add New Student")
                print("3. Update student email")
                print("4. Delete student")
                print("5. Exit")

                print()
                # Get user choice 
                choice = input("Enter your choice (1-5): ")
                print()


                if choice == '1':
                    db.getAllStudents()

                elif choice == '2':
                    first_name = input("Enter first name: ")
                    last_name = input("Enter last name: ")
                    email = input("Enter email: ")
                    enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")

                    db.addStudent(first_name, last_name, email, enrollment_date)
                
                elif choice == '3':
                    student_id = input("Enter student ID to update email: ")
                    new_email = input("Enter new email: ")

                    db.updateStudentEmail(student_id, new_email)

                elif choice == '4':
                    student_id = input("Enter student ID to delete student: ")

                    db.deleteStudent(student_id)

                elif choice == '5':
                    print("Exiting...")
                    db.disconnect()
                    break

                else:
                    print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"An error occurred: CANNOT CONNECT TO DB {e}")

# ==============================================================================================
# Run the main function if this script is executed directly
if __name__ == "__main__":
        main()