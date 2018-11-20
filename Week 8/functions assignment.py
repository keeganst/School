employee_list = []
employee_full = []
flag = False
def new_employee(employee_ID, employee_Name, employee_address, employee_email):
    employee_list.append({'Employee ID': employee_ID, 'Employee Name': employee_Name, 'Employee Email': employee_email, 'Employee Address' : employee_address})
    return employee_list

while not flag:
    employee_ID = input("Please enter the employee's ID ")
    employee_Name = input("Please enter the employees name ")
    employee_address = input("Please enter the employees address ")
    employee_email = input("Please enter the employees email ")


    escape = input("Would you like to enter another employee?(Y/N) ")

    if escape == "Y":
        continue
    else:
        break
    employee_list = new_employee(employee_ID, employee_Name, employee_address, employee_email)

print(employee_list)