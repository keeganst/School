#Creating the input variable
Employee_ID = input("Please enter your employee ID ")

if Employee_ID:
    try:
        int(Employee_ID)
        if len(Employee_ID) <= 7:
            Employee_name = input("Please enter your Name ")
            if Employee_name.isalpha():
                Employee_Email = input("PLease enter your email ")
                if Employee_Email.isalnum():
                    Employee_Address = input("Please enter your address ")
                    if Employee_Address.isalpha():
                        print("Hello," + Employee_name + " Your Employee ID is " + Employee_ID + ", your email is " + Employee_Email + " Your address is " + Employee_Address)
                    else:
                           print("Hello," + Employee_name + " Your Employee ID is " + Employee_ID + ", your email is " + Employee_Email +  " You did not provide an address.")
                else:
                    print("That isnt a valid email")
            else:
                print("that is a valid name")
        else:
            print("that isnt a valid ID")
    except:
        print("That isnt a valid ID")
else:
    print(" ")