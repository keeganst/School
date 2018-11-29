
#list for user input and a list for checking strings
college_records = []

class student():
    def __init__ (self, first_name,last_name,student_id,course_type, individual_type):
        """initializing student variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.student_ID = student_ID
        self.course_type = course_type
        self.individual_type = individual_type

    def get_student_info(individual_type):
        """gathering student information"""
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")
        student_id = input("Please enter your student ID ")
        course_type = input("Please enter your course of study ")
        college_records.append({'ID': student_id, 'First Name': first_name, 'Course type': course_type})

class instructor():
    def __init__ (self, first_name,last_name,inst_ID, inst_grad, individual_type):
        """initializing inscructor variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.inst_ID = inst_ID
        self.int_grad = course_type
        self.individual_type = individual_type

    def get_instructor_info(individual_type):
        """initializing instructor variables"""
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your first name: ")
        inst_ID = input("please enter your instructor ID ")
        inst_grad = input("PLease enter the last college you graduated from ")
        college_records.append({'ID': inst_ID, 'First Name': first_name, 'Graduation Place': inst_grad})



class validate(student,instructor):
    """validation class"""
    def __init__(self, first_name,last_name,student_id,course_type,inst_ID, inst_grad):
        """initializing variables"""
        super().__init__(first_name,last_name,student_id,course_type,inst_ID, inst_grad)
        self.bad_chars = ("[","]","\n","!","@","#","$","%","^","&","*","(",")","-","_","+","/","'","|","{","}",">","?")

    def check_student_ID(student_id):
        """checking the student ID"""
        flag = False
        while not flag:
            if self.student_id:
                try:
                    int(student_id)
                    if len(student_id) <= 7:    
                        flag = True
                    else:
                        student_id = input("Student ID was not properly formatted. Please try again: ")
                except:
                    flag = False
                
    def check_inst_ID(inst_ID):
        """checking the instructor ID"""
        flag = False
        while not flag:
            if self.inst_ID:
                try:
                    int(inst_ID)
                    if len(inst_ID) >= 5:    
                        flag = True
                    else:
                        inst_ID = input("Instructor ID was not properly formatted. Please try again: ")
                except:
                    flag = False
                    
    def check_first_name(first_name):
        """checking the first name"""
        str(first_name)
        self.bad_chars = ("[","]","\n","!","@","#","$","%","^","&","*","(",")","-","_","+","/","'","|","{","}",">","?")
        for char in self.bad_chars:
            if char in first_name:
                first_name = input("Your first name was improperly formatted please try again")
            else:
                continue

    def check_last_name(last_name):
        """checking the last name"""
        str(last_name)
        self.bad_chars = ("[","]","\n","!","@","#","$","%","^","&","*","(",")","-","_","+","/","'","|","{","}",">","?")
        for char in self.bad_chars:
            if char in last_name:
                last_name = input("Your first name was improperly formatted please try again")
            else:
                continue


flag = False
#Gathering the first of the information
while not flag:
    individual_type = input("Are you a Instructor(I) or a Student(S) ")
    str(individual_type)

    if  individual_type == "S":
        student.get_student_info("S")
        
    elif individual_type == "I" :
        instructor.get_instructor_info("I")
    else:
        individual_type = input("Please enter I for instructor or S for student ")

    escape = input("Would you like to enter another user Y/N? ")
    
    if escape == "Y":
        continue
    else:
       break


