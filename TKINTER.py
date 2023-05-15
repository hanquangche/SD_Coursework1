# Incorporate Libraries with pre-defined functionality for program to run
import csv
import os
import tkinter as tk

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
# read all file
def readall():
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        cases = []
        for row in reader:
            cases.append(row)
        return cases

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

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# Creating a menu system
print("Greetings and Welcome to the ACME AMI Institutions System.")

# -------------------------------------------------------------------------
# menu for creation of case
def createmenu():
    date_case = date_entry.get()
    s_name = name_entry.get()
    m_name = module_name_entry.get()
    m_code = module_code_entry.get()
    m_leader = module_leader_entry.get()
    allegation = allegation_entry.get()
    outcome = outcome_entry.get()
    new_record = create_record(date_case, s_name, m_name, m_code, m_leader, allegation, outcome)
    print(new_record)

# -------------------------------------------------------------------------
# menu for reading cases
def readmenu():
    all_cases = readall()
    for cases in all_cases:
        print()
        print(cases)

# -------------------------------------------------------------------------
# menu for updating a case
def updatemenu():
    choice = id_entry.get()
    date_case = date_entry.get()
    s_name = name_entry.get()
    m_name = module_name_entry.get()
    m_code = module_code_entry.get()
    m_leader = module_leader_entry.get()
    allegation = allegation_entry.get()
    outcome = outcome_entry.get()
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
    id_text = id_entry.get()
    if delete_record(id_text):
        print(f"\nCase {id_text} deleted successfully.")
    else:
        print(f"\nCase {id_text} not found.")


# -------------------------------------------------------------------------

# program start
root = tk.Tk()
root.title("Case Information")

# Create Labels
id_label = tk.Label(root, text="ID:")
id_label.grid(row=0, column=0, padx=5, pady=5)

date_label = tk.Label(root, text="Date of Case:")
date_label.grid(row=1, column=0, padx=5, pady=5)

name_label = tk.Label(root, text="Student Name:")
name_label.grid(row=2, column=0, padx=5, pady=5)

module_name_label = tk.Label(root, text="Module Name:")
module_name_label.grid(row=3, column=0, padx=5, pady=5)

module_code_label = tk.Label(root, text="Module Code:")
module_code_label.grid(row=4, column=0, padx=5, pady=5)

module_leader_label = tk.Label(root, text="Module Leader:")
module_leader_label.grid(row=5, column=0, padx=5, pady=5)

allegation_label = tk.Label(root, text="Allegation:")
allegation_label.grid(row=6, column=0, padx=5, pady=5)

outcome_label = tk.Label(root, text="Outcome of Case:")
outcome_label.grid(row=7, column=0, padx=5, pady=5)

# Create Textboxes
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=5, pady=5)

date_entry = tk.Entry(root)
date_entry.grid(row=1, column=1, padx=5, pady=5)

name_entry = tk.Entry(root)
name_entry.grid(row=2, column=1, padx=5, pady=5)

module_name_entry = tk.Entry(root)
module_name_entry.grid(row=3, column=1, padx=5, pady=5)

module_code_entry = tk.Entry(root)
module_code_entry.grid(row=4, column=1, padx=5, pady=5)

module_leader_entry = tk.Entry(root)
module_leader_entry.grid(row=5, column=1, padx=5, pady=5)

allegation_entry = tk.Entry(root)
allegation_entry.grid(row=6, column=1, padx=5, pady=5)

outcome_entry = tk.Entry(root)
outcome_entry.grid(row=7, column=1, padx=5, pady=5)

#Buttons
create_button = tk.Button(root, text="Create", command=createmenu)
create_button.grid(row=8, column=0, padx=5, pady=5)

read_button = tk.Button(root, text="Read", command=readmenu)
read_button.grid(row=8, column=1, padx=5, pady=5)

update_button = tk.Button(root, text="Update", command=updatemenu)
update_button.grid(row=8, column=2, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete", command=deletemenu)
delete_button.grid(row=8, column=3, padx=5, pady=5)

root.mainloop()