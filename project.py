# CNS1001 - Introduction to Programming
# Project 2
# student grade tracker
# members : Xavier Subratie   (2509139) - project lead, architecture
#           Ethan Eubanks     (2509775) - lead dev (core logic)
#           Rodaine Wuarrie   (2409674) - dev (data & validation)
#           Rajali Burrell    (2403230) - QA & Testing lead
#           Mikayliea Edwards (2403230) - documentation lead
#           David Maxwell     (insert your id here, david) - presentation & demo lead

# main data structure ~ holds everything, list of directories.
students_data []

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

def main():
    """the main loop of the program"""
    print("Welcome to the Student Grade Tracker!")
    
    while True:
        display_menu()
        choice = input("Enter choice: ")
        
        if choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            # Placeholder for future functions
            print(f"Option {choice} is not yet implemented.")

if __name__ == "__main__":
    main()