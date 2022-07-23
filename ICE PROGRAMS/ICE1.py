#Martin Barber - 100368442
#Sept 15th, 2021
#ICE 1 - Student information
#This will get student information and result what you typed and how many semesters you have left

from os import system

system("title Student Information - Martin Barber")

#Getting students first name
first_name = input("Please enter your name: ")

#Getting course you are in
course_name = input("Please enter the course you are in: ")

#Asking how many semesters you have in your course
semester_total = input("How many semesters does your course require: ")

#What semester are you in
current_semester = input("What semester are you in: ")

#convert semester_total and semester_current to integer
semester_total = int(semester_total)
current_semester = int(current_semester)

#Clears the console above
system("cls")

#calculate how many semesters are left to complete
#stores the result in a variable
semester_remaining = semester_total - current_semester

#display information to user
print("Name: " + first_name)
print("Course Name: " + course_name)
print("Course Duration: " + str(semester_total))
print("Current Semester: " + str(current_semester))
print("Semesters Remaining: " + str(semester_remaining) + " Semesters")

input("Press ENTER to exit: ")
