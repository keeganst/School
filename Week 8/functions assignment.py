
def check_ID(ID_pass):
    #made a quick loop to go through and check the ID
    variable = False
    while not variable:
        try: 
            int(ID_pass)
            if len(ID_pass) >= 7:    
                return ID_pass
                variable = True 
            else:
                ID_pass = input("Employee ID was not properly formatted. Please try again: ")
        except:
            ID_pass = input("Employee ID was not properly formatted. Please try again: ")

#checking the name input
def check_name(name_pass):
    variable = False
    while not variable:
        try: 
            str(name_pass)
            if name_pass.isalpha:    
                return name_pass
                variable = True
            else:
                name_pass = input("Your name was not properly formatted. Please try again: ")
        except:
            name_pass = input("Your name was not properly formatted. Please try again: ")

#checking the address input
def check_address(address_pass):
    variable = False
    while not variable:
        try: 
            str(address_pass)
            if address_pass.isalnum:    
                return address_pass
                variable = True
            else:
                address_pass = input("Your Address was not properly formatted. Please try again: ")
        except:
            address_pass = input("Your Address was not properly formatted. Please try again: ")

#checking the email input
def check_email(email_pass):
    #list to check the email for bad characters 
    bad_chars = ['%', '$','*',')','(','&','^']
    variable = False
    while not variable:
            str(email_pass)
            for chars in bad_chars:
                if chars not in email_pass:
                    return email_pass
                    variable = True
                else:
                    email_pass = input("Your email address was not properly formatted. Please try again: ") 


#a list and variable for the while loop
employee_list = []
flag = False

#a while loop to gather input from the user.
while not flag:
    employee_ID = input("Please enter the employee's ID ")
    employee_id = check_ID(employee_ID)

    employee_Name = input("Please enter the employees name ")
    employee_Name = check_name(employee_Name)

    employee_address = input("Please enter the employees address ")
    employee_address = check_address(employee_address)

    employee_email = input("Please enter the employees email ")

    employee_list.append({'Employee ID': employee_ID, 'Employee Name': employee_Name, 'Employee Email': employee_email, 'Employee Address' : employee_address})
            
    escape = input("Would you like to enter another employee?(Y/N) ")

    if escape == "Y":
        continue
    else:
       break

print(employee_list)