import csv
import os

filename = 'data.csv'

if os.path.exists(filename):
    pass
else:
    with open(filename, 'w') as f:
        # Write a header row
        f.write("id, name, age, email")

# Function to read data from CSV file
def read_data():
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append(row)
        return data

# Function to write data to CSV file
def write_data(data):
    with open('data.csv', 'w', newline='') as file:
        fieldnames = ['id', 'name', 'age', 'email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Function to create a new record
def create_record(name, age, email):
    data = read_data()
    if not data:
        new_id = 1
    else:
        new_id = int(data[-1]['id']) + 1
    new_record = {'id': new_id, 'name': name, 'age': age, 'email': email}
    data.append(new_record)
    write_data(data)
    return new_record

# Function to read a record by ID
def read_record(id):
    data = read_data()
    for row in data:
        if int(row['id']) == id:
            return row
    return None

# Function to update a record by ID
def update_record(id, name=None, age=None, email=None):
    data = read_data()
    for row in data:
        if int(row['id']) == id:
            if name:
                row['name'] = name
            if age:
                row['age'] = age
            if email:
                row['email'] = email
            write_data(data)
            return row
    return None

# Function to delete a record by ID
def delete_record(id):
    data = read_data()
    for i, row in enumerate(data):
        if int(row['id']) == id:
            del data[i]
            write_data(data)
            return True
    return False
