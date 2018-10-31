#requirement 1
list_of_courses = ["db design & development","capstone","server virtualization","network design & implementation","project management and itil framework","systems analysis and design"]

#Requirement 2
list_of_courses.sort()

for course in list_of_courses [0:6]:
    print("I have taken " + course.upper() + " at Walsh College")

#requirement 3
list_of_courses.append("advanced programming")
list_of_courses.append("data analytics")
print("This is my course of study with upcoming courses added " + str(list_of_courses))

#requirement 4

not_needed0 = "network design & implementation"
list_of_courses.remove(not_needed0)

not_needed1 = "db design & development"
list_of_courses.remove(not_needed1)

not_needed2 = "systems analysis and design"
list_of_courses.remove(not_needed2)

not_needed3 = "server virtualization" 
list_of_courses.remove(not_needed3)

not_needed4 ="project management and itil framework" 
list_of_courses.remove(not_needed4)

not_needed5 = "capstone"
list_of_courses.remove(not_needed5)


print("I do not have to take these courses\n" + str(not_needed0) + "\n" + str(not_needed1) + "\n"  + str(not_needed2) + "\n"  + str(not_needed3)  + str(not_needed4) +"\n"  + str(not_needed5))

#requirement 5
print("I plan on taking the following courses next term \n" + str(list_of_courses))

#requirement 6
numbers = list(range(0,1001,6))

#requirement 7
print("Here are twenty numbers divisble by six")

for number in numbers[0:21]:
    print(number)

#requirement 8
maximum = max(numbers)

#requirement 9
print("The maximum value in the list is " + str(maximum))

#requirement 10
summation = sum(numbers[10:51])
print("here are several values in the list " + str(summation))

list_of_courses = numbers[:]
