"""
Name: Danial Qasim
File Name: student_gpa_authentication.py
Description: This program takes students' names along with their GPAs to analyze and determine whether or not they 
qualify for the Dean's List (3.5+ GPA) or the Honor Roll (3.25+ GPA).
Variables:
    last_name (String): Holds student's last name.
    first_name (String): Holds student's first name.
    gpa (Float): Holds a student's grade point average (GPA).
"""

while True:
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
    
    if last_name == 'ZZZ':
        break
        
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print(f"Congratulations {first_name} {last_name}! You've made the Dean's List!")
    elif gpa >= 3.25:
        print(f"Great work {first_name} {last_name}, you have made the Honor Roll!")
    else:
        print(f"{first_name} {last_name} does not qualify for the Honor Roll or Dean's List.")