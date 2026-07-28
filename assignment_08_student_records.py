# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")

def add_student(students):
    """
    Prompts the user to enter a student's name, ID, and a list of scores.
    Saves the data as a dictionary and appends it to the students list.
    """
    name = input("Student name: ")
    
    try:
        student_id = int(input("Student ID: "))
        num_scores = int(input("How many scores? "))
        
        if num_scores < 0:
            print("Error: Number of scores cannot be negative.")
            return
            
        scores = []
        for i in range(1, num_scores + 1):
            score = float(input(f"Enter score {i}: "))
            # Convert to int if it's a whole number to match example output cleanly
            if score.is_integer():
                score = int(score)
            scores.append(score)
            
        # Create the dictionary for the new student
        student = {
            "name": name,
            "id": student_id,
            "scores": scores
        }
        
        students.append(student)
        print(f'Student "{name}" added successfully.')
        
    except ValueError:
        print("Error: ID and scores must be valid numbers.")

def display_all_students(students):
    """
    Prints a formatted table showing all students' information.
    """
    if not students:
        print("No students have been added yet.")
        return
        
    # Print table header
    print("-" * 65)
    # Using f-string formatting to align columns 
    # (< left aligns, > right aligns, number sets width)
    print(f"{'Name':<20} {'ID':<15} {'Scores':<20} {'Average':<10}")
    print("-" * 65)
    
    for student in students:
        name = student["name"]
        student_id = student["id"]
        scores = student["scores"]
        
        # Format the list of scores as a comma-separated string
        scores_str = ", ".join(str(s) for s in scores)
        
        # Calculate the average score safely
        if len(scores) > 0:
            average = sum(scores) / len(scores)
            avg_str = f"{average:.2f}"
        else:
            avg_str = "0.00"
            
        print(f"{name:<20} {student_id:<15} {scores_str:<20} {avg_str:<10}")
        
    print("-" * 65)

def calculate_average_score(students):
    """
    Prompts for a student ID, finds the student, and displays their average score.
    """
    if not students:
        print("The system is currently empty.")
        return
        
    try:
        search_id = int(input("Enter student ID: "))
        
        # Search for the student in the list
        found = False
        for student in students:
            if student["id"] == search_id:
                found = True
                scores = student["scores"]
                
                if len(scores) > 0:
                    average = sum(scores) / len(scores)
                    print(f"{student['name']}'s average score: {average:.2f}")
                else:
                    print(f"{student['name']} has no scores recorded.")
                break
                
        if not found:
            print("Error: Student ID not found in the system.")
            
    except ValueError:
        print("Error: Please enter a valid numeric ID.")

def main():
    """
    Main loop that drives the Student Record Management System.
    """
    # The master list storing all student dictionaries
    students = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        print() # Add an empty line for cleaner output spacing
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_all_students(students)
        elif choice == '3':
            calculate_average_score(students)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()