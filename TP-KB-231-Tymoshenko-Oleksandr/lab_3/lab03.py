class Student:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}"


class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        self.students = [s for s in self.students if s.name != name]

    def update_student(self, name, new_phone):
        for student in self.students:
            if student.name == name:
                student.phone = new_phone

    def list_students(self):
        if not self.students:
            print("No students in the list.")
        else:
            for student in self.students:
                print(student)


class FileManager:
    @staticmethod
    def load_from_csv(file_name, student_list):
        import csv
        try:
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header
                for row in reader:
                    name, phone = row
                    student_list.add_student(Student(name, phone))
        except FileNotFoundError:
            print(f"File {file_name} not found. Starting with an empty list.")

    @staticmethod
    def save_to_csv(file_name, student_list):
        import csv
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone"])
            for student in student_list.students:
                writer.writerow([student.name, student.phone])


if __name__ == "__main__":
    student_list = StudentList()

    input_file = input("Enter the input CSV file name: ")
    FileManager.load_from_csv(input_file, student_list)

    while True:
        print("\nMenu:")
        print("1. Add student")
        print("2. Remove student")
        print("3. Update student")
        print("4. List students")
        print("5. Save and exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            phone = input("Enter student phone: ")
            student_list.add_student(Student(name, phone))
        elif choice == "2":
            name = input("Enter the name of the student to remove: ")
            student_list.remove_student(name)
        elif choice == "3":
            name = input("Enter the name of the student to update: ")
            new_phone = input("Enter the new phone number: ")
            student_list.update_student(name, new_phone)
        elif choice == "4":
            student_list.list_students()
        elif choice == "5":
            output_file = input("Enter the output CSV file name: ")
            FileManager.save_to_csv(output_file, student_list)
            print("Data saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
