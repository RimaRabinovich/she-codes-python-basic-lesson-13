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
            with open('employee_file.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row == []:
                        continue
                    else:
                        emp_list.append(row)
            for i in emp_list:
                if i[0] == user_id:
                    user_name = i[1]
            if user_name == '':
                raise NoSuchID()
        except NoSuchID:
            print('ERROR: There is no such ID in the employee file.')
        else:
            user_date = (date.today()).strftime("%d/%m/%Y")
            user_time = (datetime.now()).strftime("%H:%M:%S")
            return user_id, user_name, user_date, user_time

def generate_report_of_employee():
    print("\n~~Generate attendance report~~")
    while True:
        try:
            user_id = input("Enter employee's ID: ")
            with open('attendance_file.txt','r') as readFile:
                att_list = readFile.readlines()
            emp_att = []
            for i in att_list:
                if user_id in i:
                    emp_att.append(i)
            if len(emp_att) == 0:
                raise NoSuchID()
        except NoSuchID:
            print('ERROR: There is no such ID in the employee file.')
        else:
            with open('attendance_report.txt','w') as writeFile:
                for i in emp_att:
                    writeFile.write(i)
                break

def generate_report_current_month():
    month = str((datetime.today()).month)
    with open('attendance_file.txt','r') as readFile:
        att_list = readFile.readlines()
    with open('Monthly_attendance.txt','w') as writeFile:
        for i in att_list:
            i = i.split(' ')
            i[2] = i[2].split('/')
            if i[2][1] == month:
                i[2] = ' '.join(i[2])
                i = ' '.join(i)
                writeFile.write(i)

def generate_report_late_att():
    late = datetime.now()
    late = late.replace(hour = 9, minute = 30, second = 0, microsecond = 0)
    late = late.time()
    with open('attendance_file.txt','r') as readFile:
        att_list = readFile.readlines()
    with open('late_attendance.txt','w') as writeFile:
        for i in att_list:
            i = i.split(' ')
            i[2] = i[2].split('/')
            i[3] = i[3].strip()
            i[3] = i[3].split(':')
            hour = datetime(int(i[2][2]),int(i[2][1]),int(i[2][0]),int(i[3][0]),int(i[3][1]),int(i[3][2]))
            hour = hour.time()
            if hour > late:
                i[3] = ' '.join(i[3])
                i[2] = ' '.join(i[2])
                i = ' '.join(i)
                writeFile.write(i+'\n')


def main():
    while True:
        print('\nWhat would you like to do?\n'
              'a. Mark Attendance\n'
              'b. Generate attendance report of an employee\n'
              'c. Generate attendance report of all employees in the current month\n'
              'd. Generate attendance report of all employees who were late (after 09:30)\n'
              'e. Exit program')
        ans = input("\nYou're choice: ")
        if ans == 'a':
            user_id, user_name, user_date, user_time = search_id_in_file()
            with open('attendance_file.txt','a') as attFile:
                attFile.write(user_id+' '+user_name+' '+user_date+' '+user_time+'\n')
        if ans == 'b':
            generate_report_of_employee()
        if ans == 'c':
            generate_report_current_month()
        if ans == 'd':
            generate_report_late_att()
        if ans == 'd':
            break


if __name__ == '__main__':
    main()
