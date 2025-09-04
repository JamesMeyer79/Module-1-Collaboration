#James Meyer
#Module 2 Lab - Case Study
#This app will take the student's last name, the first name, their gpa as a float, then determine if they made the deans list or honor roll. 
# To make deans a student will need a 3.5. To make honor roll they will need a 3.25. 
# It will the display the students name, gpa, and if they made the deans list, honor roll, or if they did not.
#The program will end when "ZZZ" is entered.

while True:
    lastname = input("Please input you last name (or input 'ZZZ' if you want to quit):")
    if lastname == "ZZZ":
        break

    firstname = input("Please input your first name:")

    gpa = float(input("Please enter your GPA:"))

    if gpa >= 3.5:
        print(f"{firstname} {lastname} (GPA: {gpa}) You made the Dean's list.")
    elif gpa >= 3.25:
        print(f"{firstname} {lastname} (GPA: {gpa}) You made the honor roll.")
    else:
        print(f"{firstname} {lastname} (GPA: {gpa}) You did not make the dean list or honor roll.")