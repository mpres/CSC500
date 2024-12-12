#Michael Presley Module 5 (Critical Thinking ) 12/10/24 

# Part 2, Book store book cost calculation

#Please enter how many books you have purchased

booksPurchased = int(input("Please enter the amount books you purchased this month..."))

#let's do a if elif to find the amount of books entered

if booksPurchased == 0:
  print("You have earned 0 points, because you didn't purchase any books!")
elif booksPurchased < 2:
  print("You have earned 0 points (you only bought 1 book, so don't be upset :) ")
elif booksPurchased < 4:
  print("You have earned 5 points")
elif booksPurchased < 6:
  print("You have earned 15 points")
elif booksPurchased < 8:
  print("You have earned 30 points")
elif booksPurchased >= 8:
  print("Good job! You have earned 60 points!")



  



