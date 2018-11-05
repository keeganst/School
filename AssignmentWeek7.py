
#requirement 1
employee_list = [1121, "Jackie Grainger", 22.22, 1122, "Jignesh Thrakkar", 25.25, 1127, "Dion Green", 28.75, False, 24.32, 1132, "Jacob Gerber", "Sarah Sanderson", 23.45, 1137, True,
 "Brandon Heck", 1138, 25.84, True, 1152, "David Toma", 22.65, 23.75, 1157, "Charles King", False, "Jackie Grainger", 1121, 22.22, False, 22.65, 1152, "David Toma"]
employee_name = []
employee_wage = []
employee_info = []

for employee in employee_list:
    if employee is str:
         employee_name.insert(employee)
    elif employee is int:
        employee_info.append(employee)
    elif employee is float:
        employee_wage.append(employee)

print(employee_name)
print(employee_info)
print(employee_wage)