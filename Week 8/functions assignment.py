def check_employee(ID_pass, name_pass, address_pass, email_pass):
    bad_chars = ["%", "$", "*",")","(","&","^","#"]
    if ID_pass:
        int(ID_pass)
        if len(ID_pass) >= 7:    
            employee_list.append({'Employee ID' : ID_pass})
        else:
            ID_pass = input("Employee ID was not properly formatted. Please try again: ")
    elif name_pass:
        str(name_pass)
        if name_pass.isalpha:    
            employee_list.append({'Name' : name_pass})
        else:
            name_pass = input("Your name was not properly formatted. Please try again: ")
    elif address_pass:
        str(address_pass)
        if address_pass.isalnum:    
            employee_list.append({'Employee Address' : address_pass})
        else:
            address_pass = input("Your address was not properly formatted. Please try again: ") 
    elif email_pass:
        str(email_pass)
        for chars in bad_chars:
            if chars not in email_pass:
                employee_list.append({'Employee Email' : email_pass})
            else:
               email_pass = input("Your email address was not properly formatted. Please try again: ")  


employee_list = []
employee_pass = []
flag = False





while not flag:
    employee_ID = input("Please enter the employee's ID ")
    employee_Name = input("Please enter the employees name ")
    employee_address = input("Please enter the employees address ")
    employee_email = input("Please enter the employees email ")

    check_employee(employee_ID, employee_Name, employee_address, employee_email)
            
    escape = input("Would you like to enter another employee?(Y/N) ")

    if escape == "Y":
        continue
    else:
       break

print(employee_list)