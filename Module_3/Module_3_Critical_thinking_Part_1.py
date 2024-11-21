# Mpresley 11/20/24, Module 3 CSC500, adding up a total meal

# Step 1, set teh tip_percentage and tax_rate (these are hard coded values)

tip_percentage  = .18 

tax_rate = .08


# Step 2 , get the user to enter the amount of the total meal

print("Please enter the cost of the meal without tip or tax")
meal_cost = float(input())

# Step 3, calculate the ticket items
tip = meal_cost * tip_percentage

tax = meal_cost * tax_rate

total = meal_cost + tax + tip

# Step 4 output the meal cost 
print("Meal tickets item break down as")
print("TIP = $",round(tip,2))
print("TAX = $",round(tax,2))
print("MEAL = $",round(meal_cost,2))
print("----------------")
print("TOTAL = $",round(total,2))

