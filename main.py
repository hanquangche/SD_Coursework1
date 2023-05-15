# Incorporate Libraries with pre-defined functionality for program to run
import csv
import os

# -------------------------------------------------------------------------
# Checks if CSV already exists, and creates one if there is not one present.
filename = 'database.csv'

if os.path.exists(filename):
    pass
else:
    with open(filename, 'w') as f:
        f.write("id, Date of Case, Student Name, Module Name, Module Code, Module Leader, Allegation, Outcome of Case")

# -------------------------------------------------------------------------
# Function to read data from CSV file
def read_data():
    with open('database.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append(row)
        return data

# -------------------------------------------------------------------------
# Function to write data to CSV file
def write_data(data):
    with open('database.csv', 'w', newline='') as file:
        fieldnames = ['id', 'Date of Case', 'Student Name', 'Module Name', 'Module Code', 'Module Leader', 'Allegation',
                      'Outcome of Case']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# -------------------------------------------------------------------------
# Function to create a new record
def create_record(date_case, s_name, m_name, m_code, m_leader, allegation, outcome):
    data = read_data()
    if not data:
        new_id = 1
    else:
        new_id = int(data[-1]['id']) + 1
    new_record = {
        'id': new_id,
        'Date of Case': date_case,
        'Student Name': s_name,
        'Module Name': m_name,
        'Module Code': m_code,
        'Module Leader': m_leader,
        'Allegation': allegation,
        'Outcome of Case': outcome,
    }
    data.append(new_record)
    write_data(data)
    return new_record

# -------------------------------------------------------------------------
# Function to read a record by ID
def read_record(id):
    data = read_data()
    for row in data:
        if int(row['id']) == id:
            return row
    return None

# -------------------------------------------------------------------------
# Function to update a record by ID
def update_record(record_id, new_data):
    data = read_data()
    for i, record in enumerate(data):
        if record['id'] == str(record_id):
            data[i] = {'id': str(record_id), **new_data}
            write_data(data)
            return True
    return False

# -------------------------------------------------------------------------
# Function to delete a record by ID
def delete_record(record_id):
    data = read_data()
    for i, record in enumerate(data):
        if record['id'] == str(record_id):
            del data[i]
            write_data(data)
            return True
    return False

#--------------------------------------------------------------------------
# read all file
def readall():
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        cases = []
        for row in reader:
            cases.append(row)
        return cases

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# Creating a menu system
print("Greetings and Welcome to the ACME AMI Institutions System.")

# main menu
def main():
    while True:
        print("\n1. Create a Case"
              "\n2. Read a Case"
              "\n3. Update a Case"
              "\n4. Delete a Case"
              "\n5. Exit")
        userinput = input("\nPlease enter a number: ")
        try:
            userinput = int(userinput)
        except ValueError:
            print("\nError: Please enter a valid integer.")
            continue
        if userinput == 1:
            createmenu()
        elif userinput == 2:
            readmenu()
        elif userinput == 3:
            updatemenu()
        elif userinput == 4:
            deletemenu()
        elif userinput == 5:
            exit()
        else:
            print("\nError: Please enter a valid menu option.")

# -------------------------------------------------------------------------
# menu for creation of case
def createmenu():
    date_case = commacheck("Date of Incident: ")
    s_name = commacheck("Student's Name: ")
    m_name = commacheck("Module Name: ")
    m_code = commacheck("Module Code: ")
    m_leader = commacheck("Module Leader's Name: ")
    allegation = commacheck("Allegation: ")
    outcome = commacheck("Outcome (If Any): ")
    new_record = create_record(date_case, s_name, m_name, m_code, m_leader, allegation, outcome)
    print(new_record)
    main()
# -------------------------------------------------------------------------
# menu for reading cases
def readmenu():
    while True:
        print("\n1. View All Cases"
              "\n2. View Single Case"
              "\n3. Back to Menu")
        userinput = input("\nPlease enter a number: ")
        try:
            userinput = int(userinput)
        except ValueError:
            print("\nError: Please enter a valid integer.")
            continue
        if userinput == 1:
            all_cases = readall()
            for cases in all_cases:
                print()
                print(cases)
        elif userinput == 2:
            while True:
                try:
                    choice = int(input("\nEnter Case ID: "))
                    break
                except ValueError:
                    print("\nError: Please enter a valid integer.")
                    continue
            print(read_record(choice))
            main()
        elif userinput == 3:
            main()
        else:
            print("\nError: Please enter a valid menu option.")

# -------------------------------------------------------------------------
# menu for updating a case
def updatemenu():
    while True:
        try:
            choice = int(input("\nEnter Case ID: "))
            break
        except ValueError:
            print("\nError: Please enter a valid integer.")
            continue
    date_case = commacheck("Date of Incident: ")
    s_name = commacheck("Student's Name: ")
    m_name = commacheck("Module Name: ")
    m_code = commacheck("Module Code: ")
    m_leader = commacheck("Module Leader's Name: ")
    allegation = commacheck("Allegation: ")
    outcome = commacheck("Outcome (If Any): ")
    new_record = {'Date of Case': date_case, 'Student Name': s_name, 'Module Name': m_name, 'Module Code': m_code,
                  'Module Leader': m_leader, 'Allegation': allegation, 'Outcome of Case': outcome}
    if update_record(choice, new_record):
        print(new_record)
        print(f"\nRecord with id {choice} updated successfully.")
    else:
        print(f"Record with id {choice} not found.")


# -------------------------------------------------------------------------
# menu for deleting a case
def deletemenu():
    while True:
        print("\n1. Confirm Deletion"
              "\n2. Back to Menu")
        userinput = input("\nPlease enter a number: ")
        try:
            userinput = int(userinput)
        except ValueError:
            print("\nError: Please enter a valid integer.")
            continue
        if userinput == 1:
            while True:
                try:
                    choice = int(input("\nEnter Case ID: "))
                    break
                except ValueError:
                    print("\nError: Please enter a valid integer.")
                    continue
            if delete_record(choice):
                print(f"\nCase {choice} deleted successfully.")
            else:
                print(f"\nCase {choice} not found.")
                main()
        elif userinput == 2:
            main()
        else:
            print("\nError: Please enter a valid menu option.")

# -------------------------------------------------------------------------
# additional validation check for commas to ensure csv does not break
def commacheck(entry):
    while True:
        user_input = input(entry)
        if ',' in user_input:
            print("\nError! Commas are not allowed.\n")
        else:
            return user_input

# program start
main()
