import csv

class Employee:
    # each employee must have id,name,phone,age
    def __init__(self, employee_id, name, phone, age):
        self.employee_id = employee_id
        self.name = name
        self.phone = phone
        self.age = age

class ID9Digits(Exception):
    # error to be raised when user's id is not valid
    def __str__(self):
        return('ID must be 9 digits')

class NameNotValid(Exception):
    # error to be raised when user's name is not valid
    def __str__(self):
        return('Name must be composed from alphabetic characters')

class Phone10Digits(Exception):
    # error to be raised when user's phone is not valid
    def __str__(self):
        return('Phone number must be 10 digits')

class AgeNotValid(Exception):
    # error to be raised when user's age is not valid
    def __str__(self):
        return('Age must be composed from 2 digits')

class NoSuchEmployee(Exception):
    # error to be raised when employee doesn't exist in the employee file
    def __str__(self):
        return('There is no such Name/ID')

class IDalreadyInFile(Exception):
    # error to be raised when ID already exists in the employee file
    def __str__(self):
        return('ID already exists in the employee file')

def empty_employee_file():
    #creates an empty csv file with the column names
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Employee ID', 'Employee Name', "Employee's Phone", "Employee's Age"])

def check_if_id_in_file(user_id):
    lines = list()
    with open('employee_file.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            # skip empty rows
            if row == []:
                continue
            else:
                lines.append(row)
                # check if employee's id are equal to user input
                for field in row:
                    if field == user_id:
                        return True
                    else:
                        continue

def add_employee_manually():
    # a function to add employee to employee file
    print('\n~~Add employee manually~~')
    while True:
        try:
            emp_id = input("Enter employye's ID: ")
            # to return to menu
            if emp_id == 'r':
                return
            if emp_id.isdigit() == False or len(emp_id) != 9:
                raise ID9Digits()
            if check_if_id_in_file(emp_id) == True:
                raise IDalreadyInFile()
        except ID9Digits:
            print('\nERROR: ID must be 9 digits, Try again\n')
        except IDalreadyInFile:
            print("\nERROR: ID already exists in 'employee_file.csv'\n")
        else:
            break
    while True:
        try:
            emp_name = input("Enter employye's name: ")
            if emp_name == 'r':
                return
            if emp_name.isalpha() == False or len(emp_name) < 2:
                raise NameNotValid()
        except NameNotValid:
            print("ERROR: This is not a valid name, Try again")
        else:
            break
    while True:
        try:
            emp_phone = input("Enter employye's phone number: ")
            if emp_phone == 'r':
                return
            if emp_phone.isdigit() == False or len(emp_phone) != 10:
                raise Phone10Digits()
        except Phone10Digits:
            print("ERROR: Phone number must be 10 digits")
        else:
            break
    while True:
        try:
            emp_age = input("Enter employye's age: ")
            if emp_age == 'r':
                return
            if emp_age.isdigit() == False or len(str(emp_age))>2:
                raise AgeNotValid()
        except AgeNotValid:
            print("ERROR: Age must be composed from 2 digits")
        else:
            break
    #create an employee object
    employee = Employee(emp_id,emp_name,emp_phone,emp_age)
    #add employee to file
    with open('employee_file.csv', mode='a+') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow([employee.employee_id, employee.name, employee.phone, employee.age])
    print("\nemployee was added, look at 'employee_file.csv'.")

def add_employee_from_file():
    # adds employees from csv file to the employee list
    print('\n~~Add employee from file~~')
    added = 0
    try:
        file = input("Insert CSV file that contains employees to add : ")
        if file == 'r':
            return
        with open(file, mode='r') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            line_count = 0
            for row in csv_reader:
                # skip empty rows
                if line_count == 0 or row == []:
                    line_count += 1
                    continue
                else:
                    # create employee object
                    new_employee = Employee(row[0],row[1],row[2],row[3])
                    if check_if_id_in_file(row[0]) == True:
                        continue
                    # add employee to employee file
                    with open('employee_file.csv', mode='a+') as employee_file:
                        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        employee_writer.writerow([new_employee.employee_id, new_employee.name, new_employee.phone, new_employee.age])
                        added += 1
                        line_count += 1
    except FileNotFoundError:
        print("\nERROR: There's no such file : {}".format(file))
        # when a file doesn't act like csv file
    except IndexError:
        print("ERROR: Something is wrong, Please check your file. \neach employee mast have: ID, Name, Phone and Age with a delimiter of ','.")
    if added > 0:
        print("\nemployee was added, look at 'employee_file.csv'.")
    else:
        print("\nNothing was added, the employees to be added already exist in 'employee_file.csv'")

def delete_employee_manually():
    # a function to delete employee from employee file by id/name
    print("\n~~Delete employee manually~~")
    while True:
        try:
            user_input = input('Please enter employees name/id to delete: ')
            if user_input == 'r':
                return
            # a list that will include all the employees but the one to be deleted
            lines = list()
            count = 0
            with open('employee_file.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    #skip empty rows
                    if row == []:
                        continue
                    else:
                        lines.append(row)
                        # check if employee's id or name are equal to user input
                        for field in row:
                            if field == user_input:
                                count += 1
                                lines.remove(row)
            # if nothing matches user's input raise error
            if count == 0:
                raise NoSuchEmployee()
        except NoSuchEmployee:
            print("\nERROR: There is no such Name/ID\n")
        else:
            # write the employee file again without the deleted employee
            with open('employee_file.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)
            print("\nemployee was deleted, look at 'employee_file.csv'.")
            break
        
def delete_employee_from_file():
    # a function to delete employees from file with a csv file
    print("\n~~Delete employee from file~~")
    deleted = 0
    while True:
        try:
            del_emp = input("Insert CSV File that contains employees to delete : ")
            if del_emp == 'r':
                return
            # a list for the employee file to be deleted
            emp_to_delete = list()
            # a list for existing employees
            emp_list = list()
            with open(del_emp, 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    # skip empty row
                    if row == []:
                        continue
                    else:
                        emp_to_delete.append(row)
            with open('employee_file.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    # skip empty row
                    if row == []:
                        continue
                    else:
                        emp_list.append(row)
                        for i in emp_to_delete:
                            for field in row:
                                # checks if employees id to be deleted matches the existing employees - if so, delete
                                if field == i[0]:
                                    emp_list.remove(row)
                                    deleted += 1
            if deleted == 0:
                print("\nNothing was deleted, the employees to be deleted don't exist in 'employee_file.csv'")
                break
        except FileNotFoundError:
            print("\nERROR: There's no such file\n")
        else:
            # rewrite employee file
            with open('employee_file.csv', 'w') as writeFile:
                    writer = csv.writer(writeFile)
                    writer.writerows(emp_list)
            print("\nemployee was deleted, look at 'employee_file.csv'.\n")
            break



