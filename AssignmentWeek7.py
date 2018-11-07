
#requirement 1
employee_list = [1121, "Jackie Grainger", 22.22, 1122, "Jignesh Thrakkar", 25.25, 1127, "Dion Green", 28.75, False, 24.32, 1132, "Jacob Gerber", "Sarah Sanderson", 23.45, 1137, True,
 "Brandon Heck", 1138, 25.84, True, 1152, "David Toma", 22.65, 23.75, 1157, "Charles King", False, "Jackie Grainger", 1121, 22.22, False, 22.65, 1152, "David Toma"]
employee_name = []
employee_wage = []
employee_info = []
adjusted_wage = []

for employee in employee_list:
    if employee not in employee_info and employee not in employee_name and employee not in employee_wage:
        if type(employee) is str:
            employee_name.append(employee)
        elif type(employee) is int:
            employee_info.append(employee)
        elif type(employee) is float:
            employee_wage.append(employee)

for wage in employee_wage:
   adjusted_wage.append(wage*1.3)

for wage in adjusted_wage:
    if wage > 37.30:
        print("Someones salary may be a budget concern")
    
#requirement 5
underpaid_salaries = []

for wage in adjusted_wage:
    if wage > 28.15 and wage < 30.65:
        underpaid_salaries.append(wage)

#requirement 6
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

#requirement 7
#creating a condition that will tell you what % raise the employee will get and the new rate

for wage in employee_wage:
    if wage > 22 and wage < 24:
        print("This employee makes " + "$" + str(wage) + " after their 5% raise they will make " + "$" + str(wage*1.05))
    elif wage > 24 and wage < 26:
         print("This employee makes " + "$" + str(wage) + " after their 4% raise they will make " + "$" + str(wage*1.04))
    elif wage > 26 and wage < 28:
         print("This employee makes " + "$" + str(wage) + " after their 3% raise they will make " + "$" + str(wage*1.03))
    else:
         print("This employee makes " + "$" +  str(wage) + " after their 2% raise they will make " + "$" + str(wage*1.02))
print(employee_name)
print(employee_info)
print(employee_wage)
print(adjusted_wage)
print(underpaid_salaries)
print(company_raises)