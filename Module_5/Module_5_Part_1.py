#Michael Presley Module 5 (Critical Thinking ) 12/10/24 P

# Part 1, Outer and inner loop program

#Please enter the amount of years

print("Welcome to the Weather Calculator program! Please enter the number of years to analyze ")

years = int(input())

months = 12

weather_results = []

m_dict = {0:"January",1:"February",2:"March",3:"April",4:"May",5:"June",6:"July",7:"August",8:"September",9:"October",10:"November",11:"December"}

for y in range(years):
  for m in range(months):
      txt = "Please enter the total rain fall in inches for the month of " + m_dict[m] + " for year " + str(y+1) + " "
      entry = float(input(txt))
      weather_results.append(entry)

total_inches_of_rain = sum(weather_results)
total_months = len(weather_results)
print("")
print("The total inches of rain was ", total_inches_of_rain)
print("The total amount of months used in this calculation was ", total_months)
print("")
#print("The total inches of rain for ", y , " years was ", sum(weather_results))
#print("The total amount of months used in this calculation was " years * 12)

for m in range(months):
  rainfall_for_month_of_X = weather_results[m::12]
  rainfall_avg = sum(rainfall_for_month_of_X)/len(rainfall_for_month_of_X)
  print(f"Rainfall average for {m_dict[m]} was {rainfall_avg} inches")



