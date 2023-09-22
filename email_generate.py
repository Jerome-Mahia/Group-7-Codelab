import pandas as pd


def generate_email_addresses(file_path):
    # Read the Excel file
    sheets = pd.read_excel(file_path, sheet_name=['3C', '3B'])

    # Combine the sheets into a single DataFrame
    df = pd.concat(sheets, ignore_index=True)

    # Create a list to store the generated email addresses
    email_addresses = []
    csv_tsv_data=[]

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Extract the student names
        student_name = row['Student Name']

        # Split the student names by space
        names = student_name.split()

        # Extract the first and last names
        first_name = names[0]
        last_name = names[-1]

        # Generate the email address
        email = first_name[0].lower() + last_name.lower()

        # Remove special characters from the email address
        email = ''.join(e for e in email if e.isalnum() or e.isspace())

        # Append the student name and email address to the list
        email_addresses.append(f"Student Name: {student_name} - Email address: {email+ '@gmail.com'}")

        # Append
        csv_tsv_data.append({'Student Name': student_name, 'Email Address': email + '@gmail.com'})

    # Convert the list to a DataFrame
    email_df = pd.DataFrame(csv_tsv_data, columns=['Student Name', 'Email Address'])

    # Save the DataFrame as TSV (Tab-Separated Values)
    email_df.to_csv('email_addresses.tsv', sep='\t', index=False)

    # Save the DataFrame as CSV (Comma-Separated Values)
    email_df.to_csv('email_addresses.csv', index=False)

    # Return the list of email addresses
    return email_addresses


file_path = 'Testfiles.xlsx'
email_addresses = generate_email_addresses(file_path)

# Print the email addresses
for email_address in email_addresses:
    print(email_address)