#Mpresley 11/20/24, Module 3 CSC500, creating a 24 hour clock and predict the time after adding hours

#Step 1, calculate the current time in hours

print("Please enter the hour of the current time in 24 hour notation")
current_hour = int(input())
if current_hour > 23 or current_hour < 0:
	print("Error, the current hour must be 0 and 23")
	exit()

print("Please enter the amount of hours to calculate the future time")

hour = int(input())

hour_result = (hour+current_hour)%24


print("The hour at this time is ",hour_result)
