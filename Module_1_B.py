# Mpresley 11/12/24, Module 1 CSC500, multiplying and dividing two numbers

print("Please enter two numbers to 'Multiply' and 'Divide'")

#Get first number
print("Enter Number 1")
number1 = int(input())

#Get second number
print("Now enter Number 2, this number must not be zero")
number2 = int(input())

while number2 == 0:
	print("Number 2 can't be zero, please enter it again")
	number2 = int(input())

#Calculate the answer for Multiplication
answer = number1 * number2

#Print out the answer for Multiplication
print(f'Multipling {number1} and {number2} equals {answer}')

#Calcuate the answer for Division
answer = number1 / number2

print(f'Dividing {number1} by {number2} equals {answer}')
 
