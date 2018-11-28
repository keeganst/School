
class person():
    """ Class for the default person"""
    def __init__(self, individual_type, first_name, last_name):

        self.individual_type = individual_type
        self.first_name = first_name
        self.last_name = last_name
    
class student(person):
    """class for the student"""
    def __init__(self, individual_type, first_name, last_name):
        super().__init__(first_name, last_name)
        self.student_id = input("Please enter your student ID")


class instructor(person):
    """class for the instructor """
    def __init__(self, individual_type, first_name, last_name):
        super().__init__(first_name, last_name)
        self.instructor_ID = input("Please enter your Instructor ID")

class validator():
    def __init__(self, first_name, last_name):
        self.individual_type = individual_type
        self.first_name = first_name
        self.last_name = last_name
    
    def check_first_name():
        bad_chars = [ '!', '@', '#' ,'$', '%', '^', '&', '*', '(', ')', '_', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', ')']
        variable = False
        while not variable:
            str(self.first_name)
            for chars in bad_chars:
                if chars not in self.first_name:
                    variable = True
                else:
                    self.first_name = input("Your first name was not formatted properly please try again ") 



flag = False
#Gathering the first of the information
while not flag:
    individual_type = input("Are you a Instructor(I) or a Student(S)")
    str(individual_type)

    if individual_type == "I" or individual_type == "S":
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your first name: ")
        validator(first_name, last_name)
    else:
        individual_type = input("Please enter I for instructor or S for student")

    if individual_type == "I":

    elif individual_type == "S":


    escape = input("Would you like to enter another user Y/N?")
    
    if escape == "Y":
        continue
    else:
       break


