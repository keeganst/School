#i brought over the code from the other assignment

employee_list = [1121, "Jackie Grainger", 22.22, 1122, "Jignesh Thrakkar", 25.25, 1127, "Dion Green", 28.75, False, 24.32, 1132, "Jacob Gerber", "Sarah Sanderson", 23.45, 1137, True,
 "Brandon Heck", 1138, 25.84, True, 1152, "David Toma", 22.65, 23.75, 1157, "Charles King", False, "Jackie Grainger", 1121, 22.22, False, 22.65, 1152, "David Toma"]
employee_name = []
employee_wage = []
employee_numbers = []
adjusted_wage = []

for employee in employee_list:
    if employee not in employee_numbers and employee not in employee_name and employee not in employee_wage:
        if type(employee) is str:
            employee_name.append(employee)
        elif type(employee) is int:
            employee_numbers.append(employee)
        elif type(employee) is float:
            employee_wage.append(employee)

for wage in employee_wage:
   adjusted_wage.append(wage*1.3)

company_raises = []

for wage in employee_wage:
    if wage > 22 and wage < 24:
        company_raises.append(wage * 1.05)
    elif wage > 24 and wage < 26:
        company_raises.append(wage * 1.04)
    elif wage > 26 and wage < 28:
        company_raises.append(wage * 1.05)
    else:
        company_raises.append(wage * 1.02)

#Creating the dictionary

employee_final = []

#count index variable
count_index = 0
output = ""
#loops to add the data into the dictionary
for employee in employee_numbers:
    employee_final.append({'Employee Number' : employee, 'Name': employee_name[count_index],
                            'Employee Salary': employee_wage[count_index], 'Adjusted Salary':adjusted_wage[count_index],
                            'Employee Raise': company_raises[count_index] })
    count_index = count_index + 1  

print(employee_final)