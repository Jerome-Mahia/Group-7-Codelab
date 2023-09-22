# import pandas as pd
# import re
#
# #Email question
# def generate_email_addresses(file_path):
#     # Read the Excel file
#     sheets = pd.read_excel(file_path, sheet_name=['3C', '3B'])
#
#     # Combine the sheets into a single DataFrame
#     df = pd.concat(sheets, ignore_index=True)
#
#     # Create a list to store the generated email addresses
#     email_addresses = []
#     csv_tsv_data=[]
#
#     # Iterate over each row in the DataFrame
#     for index, row in df.iterrows():
#         # Extract the student names
#         student_name = row['Student Name']
#
#         # Split the student names by space
#         names = student_name.split()
#
#         # Extract the first and last names
#         first_name = names[0]
#         last_name = names[-1]
#
#         # Generate the email address
#         email = first_name[0].lower() + last_name.lower()
#
#         # Remove special characters from the email address
#         email = ''.join(e for e in email if e.isalnum() or e.isspace())
#
#         # Append the student name and email address to the list
#         email_addresses.append(f"Student Name: {student_name} - Email address: {email+ '@gmail.com'}")
#
#         # Append
#         csv_tsv_data.append({'Student Name': student_name, 'Email Address': email + '@gmail.com'})
#
#     # Convert the list to a DataFrame
#     email_df = pd.DataFrame(csv_tsv_data, columns=['Student Name', 'Email Address'])
#
#     # Save the DataFrame as TSV (Tab-Separated Values)
#     email_df.to_csv('email_addresses.tsv', sep='\t', index=False)
#
#     # Save the DataFrame as CSV (Comma-Separated Values)
#     email_df.to_csv('email_addresses.csv', index=False)
#
#     # Return the list of email addresses
#     return email_addresses
#
#
# file_path = 'Testfiles.xlsx'
# email_addresses = generate_email_addresses(file_path)
#
# # Print the email addresses
# for email_address in email_addresses:
#     print(email_address)
#
# # Gender questions
#
# def generate_gender_lists(file_path):
#     # Read the Excel file
#     df = pd.read_excel(file_path)
#
#     # Initialize lists for male and female students
#     male_students = []
#     female_students = []
#
#     # Iterate over each row in the DataFrame
#     for index, row in df.iterrows():
#         # Extract the gender value
#         gender = str(row['Gender']).strip().upper()
#
#         # Check if the gender is male or female
#         if gender == 'M':
#             male_students.append(row['Student Name'])
#         elif gender == 'F':
#             female_students.append(row['Student Name'])
#
#     # Print the number of male and female students
#     print(f"Number of Male Students: {len(male_students)}")
#     print(f"Number of Female Students: {len(female_students)}")
#
#     # Return the lists of male and female students
#     return male_students, female_students
#
# def list_students_with_special_characters(file_path):
#     # Read the Excel file
#     df = pd.read_excel(file_path)
#
#     # Initialize a list for students with special characters
#     students_with_special_chars = []
#
#     # Iterate over each row in the DataFrame
#     for index, row in df.iterrows():
#         # Extract the student name
#         student_name = str(row['Student Name']).strip()
#
#         # Check if the student name contains special characters using regex
#         if re.search(r"[a-zA-Z]+'[a-zA-Z]+", student_name):
#             students_with_special_chars.append(student_name)
#
#     # Return the list of students with special characters
#     return students_with_special_chars
#
#
# file_path = 'Testfiles.xlsx'
#
# # Generate separate lists of male and female students
# male_students, female_students = generate_gender_lists(file_path)
# print('Male student  list:')
# print(male_students)
# print('Female student list:')
# print(female_students)
#
#
# # List the names of students with special characters
# students_with_special_chars = list_students_with_special_characters(file_path)
# print('Students with special characters')
# print(students_with_special_chars)