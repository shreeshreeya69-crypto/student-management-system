print("Student Management System")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
while True:
    try:
        age = int(input("Enter student age: "))
        if 1 <= age <= 100:
            break
        else:
            print("Please enter a age between 1 and 100.")
    except ValueError:
        print("Please enter a number.")


print("Student Name:", name)
print("Roll Number:", roll_no)
print("Age:", age)