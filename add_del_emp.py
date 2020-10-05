import csv

class Employee:

    def __init__(self, employee_id, name, phone, age):
        self.employee_id = employee_id
        self.name = name
        self.phone = phone
        self.age = age

class ID9Digits(Exception):
    def __str__(self):
        return('ID must be 9 digits')

class NameNotValid(Exception):
    def __str__(self):
        return('Name must be composed from alphabetic characters')

class Phone10Digits(Exception):
    def __str__(self):
        return('Phone number must be 10 digits')

class AgeNotValid(Exception):
    def __str__(self):
        return('Age must be composed from 2 digits')

class NoSuchEmployee(Exception):
    def __str__(self):
        return('There is no such Name/ID')

def empty_employee_file():
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Employee ID', 'Employee Name', "Employee's Phone", "Employee's Age"])

def add_employee_manually():
    print('\n~~Add employee manually~~')
    while True:
        try:
            emp_id = input("Enter employye's ID: ")
            if emp_id.isdigit() == False or len(emp_id) != 9:
                raise ID9Digits()
        except ID9Digits:
            print('ERROR: ID must be 9 digits, Try again')
        else:
            break
    while True:
        try:
            emp_name = input("Enter employye's name: ")
            if emp_name.isalpha() == False or len(emp_name) < 2:
                raise NameNotValid()
        except NameNotValid:
            print("ERROR: This is not a valid name, Try again")
        else:
            break
    while True:
        try:
            emp_phone = input("Enter employye's phone number: ")
            if emp_phone.isdigit() == False or len(emp_phone) != 10:
                raise Phone10Digits()
        except Phone10Digits:
            print("ERROR: Phone number must be 10 digits")
        else:
            break
    while True:
        try:
            emp_age = input("Enter employye's age: ")
            if emp_age.isdigit() == False or len(str(emp_age))>2:
                raise AgeNotValid()
        except AgeNotValid:
            print("ERROR: Age must be composed from 2 digits")
        else:
            break
    employee = Employee(emp_id,emp_name,emp_phone,emp_age)
    with open('employee_file.csv', mode='a+') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow([employee.employee_id, employee.name, employee.phone, employee.age])

def add_employee_from_file():
        print('\n~~Add employee from file~~')
        try:
            file = input("Insert employees to add CSV file: ")
            with open(file, mode='r') as file:
                csv_reader = csv.reader(file, delimiter = ',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0 or row == []:
                        line_count += 1
                        continue
                    else:
                        new_employee = Employee(row[0],row[1],row[2],row[3])
                        with open('employee_file.csv', mode='a+') as employee_file:
                            employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                            employee_writer.writerow([new_employee.employee_id, new_employee.name, new_employee.phone, new_employee.age])
                        line_count += 1
        except FileNotFoundError:
            print("ERROR: There's no such file : {}".format(file))
        except IndexError:
            print("ERROR: Something is wrong, Please check your file. \neach employee mast have: ID, Name, Phone and Age with a delimiter of ','.")

def delete_employee_manually():
    print("\n~~Delete employee manually~~")
    while True:
        try:
            user_input = input('Please enter employees name/id to delete: ')
            lines = list()
            count = 0
            with open('employee_file.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row == []:
                        continue
                    else:
                        lines.append(row)
                        for field in row:
                            if field == user_input:
                                count += 1
                                lines.remove(row)
            if count == 0:
                raise NoSuchEmployee()
        except NoSuchEmployee:
            print("ERROR: There is no such Name/ID")
        else:
            with open('employee_file.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)
                break
        
def delete_employee_from_file():
    print("\n~~Delete employee from file~~")
    while True:
        try:
            del_emp = input("Insert employees to delete CSV File: ")
            emp_to_delete = list()
            emp_list = list()
            with open(del_emp, 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row == []:
                        continue
                    else:
                        emp_to_delete.append(row)
            with open('employee_file.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row == []:
                        continue
                    else:
                        emp_list.append(row)
                        for i in emp_to_delete:
                            for field in row:
                                if field == i[0]:
                                    emp_list.remove(row)
        except FileNotFoundError:
            print("ERROR: There's no such file")
        else:
            with open('employee_file.csv', 'w') as writeFile:
                    writer = csv.writer(writeFile)
                    writer.writerows(emp_list)
                    break


def main():
    empty_employee_file()
    add_employee_from_file()
    delete_employee_manually()
    delete_employee_from_file()

if __name__ == '__main__':
    main()
