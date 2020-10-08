import add_del_emp as adl
import attendance_emp as att

def main():
    #adl.empty_employee_file()
    while True:
        print("\nWhat would you like to do? \n"
              "a. Add employee manually\n"
              "b. Add employee from file - insert CSV file\n"
              "c. Delete employee manually - insert employee's ID/name\n"
              "d. Delete employee from file - insert CSV file\n"
              'e. Mark Attendance\n'
              'f. Generate attendance report of an employee\n'
              'g. Generate attendance report of all employees in the current month\n'
              'h. Generate attendance report of all employees who were late (after 09:30)\n'
              "i. Exit program\n")
        ans = input("You're choice: ")
        if ans == 'a':
            adl.add_employee_manually()
            print("\nemployee was added, look at 'employee_file.csv'.")
        elif ans == 'b':
            adl.add_employee_from_file()
            print("\nemployee was added, look at 'employee_file.csv'.")
        elif ans == 'c':
            adl.delete_employee_manually()
            print("\nemployee was deleted, look at 'employee_file.csv'.")
        elif ans == 'd':
            adl.delete_employee_from_file()
            print("\nemployee was deleted, look at 'employee_file.csv'.")
        elif ans == 'e':
            user_id, user_name, user_date, user_time = att.search_id_in_file()
            with open('attendance_file.txt','a') as attFile:
                attFile.write(user_id+' '+user_name+' '+user_date+' '+user_time+'\n')
            print("\nattendance was marked at 'attendance_file.txt'.")
        elif ans == 'f':
            att.generate_report_of_employee()
        elif ans == 'g':
            att.generate_report_current_month()
        elif ans == 'h':
            att.generate_report_late_att()
        elif ans == 'i':
            break

if __name__ == '__main__':
    main()