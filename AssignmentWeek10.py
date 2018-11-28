class student():
    def __init__(self, first_name, last_name, student_ID, course_type):
        self.first_name = first_name
        self.last_name = last_name
        self.course_type = course_type
        self.student_ID = student_ID
    
    def get_student_ID():
        """Getting the course type"""
        self.student_ID = input("Please enter your student ID")

    def get_course_type(self):
        """Getting the course type"""
        self.course_type = input("Please enter your Program of study")


class instructor():
    def __init__(self, first_name, last_name, instructor_ID, grad_location):
        self.first_name = first_name
        self.last_name = last_name
        self.instructor_ID = instructor_ID
        self.grad_location = grad_location
    
    def get_inst_ID(self):
        self.instructor_ID = input("Please enter your Instructor ID")

    def get_grad_location(self):
        """Getting the course type"""
        self.grad_location = input("Please enter the last college you graduated from")





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
    individual_type = input("Are you a Instructor(I) or a Student(S) ")
    str(individual_type)

    if individual_type == "I" or individual_type == "S":
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your first name: ")
        validator(first_name, last_name)
    else:
        individual_type = input("Please enter I for instructor or S for student ")
    
    if individual_type == "I":
        instructor_ID = instructor.get_inst_ID()
    elif individual_type == "S":
      student_id = student.get_student_ID()

    escape = input("Would you like to enter another user Y/N? ")
    
    if escape == "Y":
        continue
    else:
       break


