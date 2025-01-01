#Mpresley 1/1/25
#Michael Presley 12/27/24 Critical Thinking Section
#  set the Instructors dictionary

Instructors_dict = {"CSC101": "Haynes", "CSC102": "Alvarado", "CSC103": "Rich", "NET110":"Burke", "COM241":"Lee"}

# set the Room Number Dictionary
Room_Number_dict = {"CSC101": "3004", "CSC102": "4501", "CSC103": "6755", "NET110":"1244", "COM241":"1441"}

# set tehe Meeting Room Number
Meeting_time_dict = {"CSC101": "8:00 a.m.", "CSC102": "9:00 a.m.", "CSC103": "10:00 a.m.", "NET110":"11:00 a.m.", "COM241":"1:00 p.m."}

#Capture Errors
course_number = input("Please Enter the a Course Number to learn more about that course:")

try:
  print(f"Course Room Number is: {Room_Number_dict[course_number]}, the Instructor is {Instructors_dict[course_number]} and the Meeting time is {Meeting_time_dict[course_number]}") 
except:
  print(course_number, " is not a registered course")
