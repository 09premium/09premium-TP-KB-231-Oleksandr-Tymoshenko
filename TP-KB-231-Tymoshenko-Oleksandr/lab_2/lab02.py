import csv
import sys

class StudentDirectory:
    def __init__(self):
        self.students = []

    def load_from_csv(self, file_name):
        """Load students from a CSV file."""
        try:
            with open(file_name, 'r') as file:
                reader = csv.DictReader(file)
                self.students = [row for row in reader]
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")

    def save_to_csv(self, file_name):
        """Save students to a CSV file."""
        if not self.students:
            print("No students to save.")
            return
        
        with open(file_name, 'w', newline='') as file:
            fieldnames = self.students[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.students)

    def add_student(self, name, phone):
        """Add a new student."""
        self.students.append({"Name": name, "Phone": phone})

    def list_students(self):
        """List all students."""
        if not self.students:
            print("No students in the directory.")
        else:
            for student in self.students:
                print(f"Name: {student['Name']}, Phone: {student['Phone']}")

if __name__ == "__main__":
    directory = StudentDirectory()

    # Check for command-line arguments
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
        directory.load_from_csv(csv_file)
    else:
        print("No input file provided. Starting with an empty directory.")

    while True:
        print("\nMenu:")
        print("1. Add student")
        print("2. List students")
        print("3. Save and exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            phone = input("Enter student phone: ")
            directory.add_student(name, phone)
        elif choice == "2":
            directory.list_students()
        elif choice == "3":
            output_file = input("Enter the name of the file to save (e.g., 'output.csv'): ")
            directory.save_to_csv(output_file)
            print("Directory saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
