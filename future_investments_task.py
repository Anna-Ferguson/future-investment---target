invest = int(input("Enter the starting investment amount: "))
pay = int(input("Enter the monthly payment amount: "))
ar  = float(input("Enter the annual interest rate (Ex 5.3): "))
year = int(input("How many years would you like to invest for: "))
mir = ar /12
month = year * 12
piece1 = ( 1 + mir)**month
piece2 = ((1 + mir)**month - 1)/ mir
piece3 = (1 + mir)
futurevalue = (invest * piece1) + (pay * piece2 * piece3)
print("Future Value: " + str(futurevalue))



#futurevalue = investment amount * (1 + monthly interest rate)**number of months + monthly payment
# ((1+ monthly interest rate)**number of months -1)/monthly interest rate * (1 + monthly interest rate)