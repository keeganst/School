

Employee_info = []
print(Employee_info)

program_running = True
count_variable = 0

while program_running:
#Start processing for employee ID
    Employee_ID = input("Please enter your Employee ID ")

    Employee_ID_ok = False

    while not Employee_ID:
        if Employee_ID:
            try:
                int(Employee_ID)
                if len(Employee_ID) >= 7:    
                    Employee_ID_ok = True
                else:
                    Employee_ID_ok = False
            except:
                Employee_ID_ok = False
        else:
            Employee_ID_ok = False
        if not Employee_ID_ok:
            Employee_ID = input("Employee ID was not properly formatted. Please try again: ") 


#end employee ID processing
#begin processing employee Name

    Employee_name = input("Please enter your name ")

    Employee_name_ok = False

    while not Employee_name_ok:
        if Employee_name:
            try:
                str(Employee_name)
                if Employee_name.isalpha:    
                    Employee_name_ok = True
                else:
                    Employee_name_ok = False
            except:
                Employee_name_ok = False
        else:
            Employee_name_ok = False
        if not Employee_name_ok:
            Employee_name = input("Your name was not properly formatted. Please try again: ") 

#end name processing
#begin email address processing

    Employee_email = input("Please enter your email address ")
    Employee_email_ok = False

    while not Employee_email_ok:
        if Employee_email:
            try:
                str(Employee_email)
                if Employee_email.isalnum:    
                    Employee_email_ok = True
                else:
                    Employee_email_ok = False
            except:
                Employee_email_ok = False
        else:
            Employee_email_ok = False
        if not Employee_email_ok:
            Employee_email = input("Your Email was not properly formatted. Please try again: ") 

#begin address processing

    Employee_address = input("Please enter your address ")
    Employee_address_ok = False

    while not Employee_address_ok:
        if Employee_address:
            try:
                str(Employee_address)
                if Employee_address.isalnum:    
                    Employee_address_ok = True
                else:
                    Employee_address_ok = False
            except:
                Employee_address_ok = False
        else:
            Employee_address_ok = False
        if not Employee_address_ok:
            Employee_address = input("Your address properly formatted. Please try again: ") 

    Employee_info.append({'Employee ID': Employee_ID, 'Employee Name': Employee_name, 'Employee Email': Employee_email, 'Employee Address' : Employee_address})
    
    count_variable = count_variable + 1

    if count_variable >= 5:
        break
    else:
        continue
print(Employee_info)


print(Employee_info)