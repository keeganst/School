# First requirement storing first name in all lowercase
string_first = 'keegan'

#Second and Fourth requirement 2 new lines and last name in all uppercase
string_lastname = "CHRISTIE\n\n"

#Variable for fourth requirement
string_quote = "\"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi\""

#variables for requirements 6 through 10
number_variable_A = 10.5
number_variable_B = 25.6
number_addition = number_variable_A + number_variable_B
number_subtraction = number_variable_A - number_variable_B
number_multiplcation = number_variable_A * number_variable_B
number_division = number_variable_A / number_variable_B 

string_month = "October"
number_day = 29 

output_variable = "\n\t\t Today is day " + str(number_day) + " of the month of" + string_month

#Third requirement 
print("Hello, " + string_first.upper() + " " + string_lastname.lower())

#fourth requirement 
print(string_quote)

#Print statements for requirements 6 through 10

print( str(number_variable_A) + " plus " + str(number_variable_B) + " equals " + str(number_addition) + "\n")
print( str(number_variable_A) + " minus " + str(number_variable_B) + " equals " + str(number_addition)+ "\n")
print( str(number_variable_A) + " multiplied by " + str(number_variable_B) + " equals " + str(number_addition)+ "\n")
print( str(number_variable_A) + " divided by " + str(number_variable_B) + " equals " + str(number_addition)+ "\n")

print(output_variable)


