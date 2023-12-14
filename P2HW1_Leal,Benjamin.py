# This program calculates and displays travel expenses
# 9/5/23
# CTI-110 P2HW1 - Travel Expense
# Benjamin Leal
#

print ('This program calculates and diplays travel expenses. \n')
budget = float(input("Enter budget:  "))
print()
destination = input("Enter trvel destination: \n")
print()
gas = float(input("How much do you think you will spend on gas?\n"))
print()
hotel = float(input("About how much do you thin you will spend on accomidations?\n"))
print()
Food = float(input("How much will you spend on food?\n"))
print()

print('-------------Travel Expenses-------------')
print("location:",destination)
print("initial budget:" ,budget)
print("\nFuel:" ,gas)
print("Accomidations:" , hotel)
print("Food:" ,Food)
