# CNS1001 - Introduction to Programming
# Project 2
# student grade tracker
# members : Xavier Subratie   (2509139) - project lead, architecture
#           Ethan Eubanks     (2509775) - lead dev (core logic)
#           Rodaine Wuarrie   (2409674) - dev (data & validation)
#           Rajali Burrell    (2007948) - QA & Testing lead
#           Mikayliea Edwards (2403230) - documentation lead
#           David Maxwell     (insert your id here, david) - presentation & demo lead

# main data structure ~ holds everything, list of directories.
students_data = []

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Student Grade Tracker ---")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. Calculate Average")
    print("4. Student Report")
    print("5. Class Report")
    print("6. Search Student")
    print("7. Class Summary")
    print("8. Save Data")
    print("9. Load Data")
    print("0. Exit")

def get_valid_input(prompt, input_type="str", min_val=None, max_val=None):
    """
    Validates user input based on type and range.
    input_type: 'str' for text, 'int' or 'float' for numbers
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue
        
        if input_type == "str":
            return user_input
        elif input_type in ("int", "float"):
            try:
                # convertsConvert to float first so it handles both int and float inputs cleanly
                value = float(user_input) 
                if input_type == "int" and not user_input.isdigit() and not (user_input.startswith('-') and user_input[1:].isdigit()):
                    # Extra check to prevent 85.5 being accepted if int was requested
                    raise ValueError 
                if min_val is not None and value < min_val:
                    print(f"Value must be at least {min_val}.")
                    continue
                if max_val is not None and value > max_val:
                    print(f"Value must be at most {max_val}.")
                    continue
                return int(value) if input_type == "int" else value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

def add_student():
    """Adds a new student to the students_data list."""
    print("\n--- Add New Student ---")
    name = get_valid_input("Enter student name: ")
    student_id = str(get_valid_input("Enter student ID: "))
    
    # Check if student ID already exists to prevent duplicates
    for student in students_data:
        if student["id"] == student_id:
            print(f"Error: A student with ID '{student_id}' already exists.")
            return
            
    new_student = {
        "name": name,
        "id": student_id,
        "grades": {}
    }
    students_data.append(new_student)
    print(f"Student '{name}' (ID: {student_id}) added successfully.")

def add_grade():
    """Adds or updates a grade for an existing student."""
    print("\n--- Add Grade ---")
    if not students_data:
        print("No students found. Please add a student first.")
        return
    
    search_term = get_valid_input("Enter student name or ID: ")
    student_found = None
    
    # Search through our list to find the matching student
    for student in students_data:
        if search_term.lower() == student["name"].lower() or search_term == student["id"]:
            student_found = student
            break
            
    if not student_found:
        print(f"Student '{search_term}' not found.")
        return
        
    course = get_valid_input("Enter course name: ")
    # Using our validation function to ensure grade is between 0 and 100
    grade = get_valid_input("Enter grade (0-100): ", input_type="float", min_val=0, max_val=100)
    
    # Save to the student's grades dictionary
    student_found["grades"][course] = grade
    print(f"Grade {grade} added for {course}.")
    
def main():
    """the main loop of the program"""
    print("Welcome to the Student Grade Tracker!")
    
    while True:
        display_menu()
        choice = input("Enter choice: ")
        
        if choice == '0':
            print("Exiting program. Goodbye!")
            break
        elif choice == '1':
            add_student()
        elif choice == '2':
            add_grade()
        else:
            print(f"Option {choice} is not yet implemented.")

if __name__ == "__main__":
    main()