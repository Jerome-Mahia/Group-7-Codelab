import pandas as pd
import re

def generate_gender_lists(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Initialize lists for male and female students
    male_students = []
    female_students = []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Extract the gender value
        gender = str(row['Gender']).strip().upper()

        # Check if the gender is male or female
        if gender == 'M':
            male_students.append(row['Student Name'])
        elif gender == 'F':
            female_students.append(row['Student Name'])

    # Print the number of male and female students
    print(f"Number of Male Students: {len(male_students)}")
    print(f"Number of Female Students: {len(female_students)}")

    # Return the lists of male and female students
    return male_students, female_students

def list_students_with_special_characters(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Initialize a list for students with special characters
    students_with_special_chars = []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Extract the student name
        student_name = str(row['Student Name']).strip()

        # Check if the student name contains special characters using regex
        if re.search(r"[a-zA-Z]+'[a-zA-Z]+", student_name):
            students_with_special_chars.append(student_name)

    # Return the list of students with special characters
    return students_with_special_chars


file_path = 'Testfiles.xlsx'

# Generate separate lists of male and female students
male_students, female_students = generate_gender_lists(file_path)
print('Male student  list:')
print(male_students)
print('Female student list:')
print(female_students)


# List the names of students with special characters
students_with_special_chars = list_students_with_special_characters(file_path)
print('Students with special characters')
print(students_with_special_chars)