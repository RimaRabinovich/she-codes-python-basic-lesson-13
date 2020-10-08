import csv
from datetime import date,datetime

class Attendance():

    def __init__(self, _date, _time, _id, _name):
        self._date = _date
        self._time = _time
        self._id = _id
        self._name = _name

class NoSuchID(Exception):
    def __str__(self):
        print('No such ID in the file')

def search_id_in_file():
    while True:
        try:
            user_id = input("Please enter employee ID: ")
            emp_list = list()
            user_name = ''
            # creates list of employees read from file
            with open('employee_file.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    # skip empty row
                    if row == []:
                        continue
                    else:
                        emp_list.append(row)
            for i in emp_list:
                # checks if the id matches
                if i[0] == user_id:
                    user_name = i[1]
            # raise error if id wasn't found
            if user_name == '':
                raise NoSuchID()
        except NoSuchID:
            print('\nERROR: There is no such ID in the employee file.\n')
        else:
            # get current date and time
            user_date = (date.today()).strftime("%d/%m/%Y")
            user_time = (datetime.now()).strftime("%H:%M:%S")
            return user_id, user_name, user_date, user_time

def mark_attendance():
    user_id, user_name, user_date, user_time = search_id_in_file()
    with open('attendance_file.txt', 'a') as attFile:
        attFile.write(user_id + ' ' + user_name + ' ' + user_date + ' ' + user_time + '\n')
    print("\nattendance was marked at 'attendance_file.txt'.")

def generate_report_of_employee():
    # creates a report for a spesific employee by id
    print("\n~~Generate attendance report~~")
    while True:
        try:
            user_id = input("Enter employee's ID: ")
            user_att_file = 'attendance_file' + '_' + user_id + '.txt'
            with open('attendance_file.txt','r') as readFile:
                att_list = readFile.readlines()
            # a list to store all employees attendance
            emp_att = []
            for i in att_list:
                if user_id in i:
                    emp_att.append(i)
            # raise error if id wasn't found
            if len(emp_att) == 0:
                raise NoSuchID()
        except NoSuchID:
            print('\nERROR: There is no such ID in the employee file.\n')
        except FileNotFoundError:
            print("\nERROR : There must be an 'attendance_file.csv' in order to generate employee's attendance report\n~~~No report was generated~~~\n~~~Back to main menu~~~")
            break
        else:
            # write report file from the created list of a spesific employee
            with open(user_att_file,'w') as writeFile:
                for i in emp_att:
                    writeFile.write(i)
                print("\nReport '{}' was generated.".format(user_att_file))
                break

def generate_report_current_month():
    while True:
        try:
            # get current month
            month = str((datetime.today()).month)
            #read attendance file to a list
            with open('attendance_file.txt','r') as readFile:
                att_list = readFile.readlines()
                # write attendence file only for the current month
        except FileNotFoundError:
            print("\nERROR : There must be an 'attendance_file.csv' in order to generate monthly attendance report\n~~~No report was generated~~~\n~~~Back to main menu~~~")
            break
        else:
            with open('Monthly_attendance.txt','w') as writeFile:
                for i in att_list:
                    # spliting each row by space and then split again with '/' in order to get only the month
                    i = i.split(' ')
                    i[2] = i[2].split('/')
                    if i[2][1] == month:
                        # join each row back to str in order to write it to file
                        i[2] = ' '.join(i[2])
                        i = ' '.join(i)
                        writeFile.write(i)
                print("\nReport 'Monthly_attendance.txt' was generated.")
                break

def generate_report_late_att():
    while True:
        try:
            # get current date and time in order to get only the time
            late = datetime.now()
            # changing the time to 9:30
            late = late.replace(hour = 9, minute = 30, second = 0, microsecond = 0)
            # getting only the time
            late = late.time()
            # create list from file
            with open('attendance_file.txt','r') as readFile:
                att_list = readFile.readlines()
        except FileNotFoundError:
            print("\nERROR : There must be an 'attendance_file.csv' in order to generate late attendance report\n~~~No report was generated~~~\n~~~Back to main menu~~~")
            break
        else:
            # write file of all late attendance
            with open('late_attendance.txt','w') as writeFile:
                for i in att_list:
                    # spliting each row in order to get date and time
                    i = i.split(' ')
                    i[2] = i[2].split('/')
                    i[3] = i[3].strip()
                    i[3] = i[3].split(':')
                    # getting the time from attendance file in a format we can use to compare
                    hour = datetime(int(i[2][2]),int(i[2][1]),int(i[2][0]),int(i[3][0]),int(i[3][1]),int(i[3][2]))
                    # getting only the time
                    hour = hour.time()
                    # get the rows that are later than 9:30
                    if hour > late:
                        # join the row back to str in order to write to file
                        i[3] = ' '.join(i[3])
                        i[2] = ' '.join(i[2])
                        i = ' '.join(i)
                        writeFile.write(i+'\n')
                print("\nReport 'late_attendance.txt' was generated.")
                break



