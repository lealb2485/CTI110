# CTI-110

# P3HW2 - Salary

# Benjamin Leal

# 10/10/23

#

name = input('Enter employees name:')
hours_worked = float(input('Enter number of hours worked:'))
Pay_Rate =  float(input('Enter employees pay rate:'))
Over_Time = hours_worked - 40
Overtime_pay = Over_Time * Pay_Rate / 0.5
RegHour_pay = Pay_Rate * hours_worked
Gross_pay = RegHour_pay + Overtime_pay


print('-----------------------------------------------')
print("\nEmployee name:",name,'\n')

print('Hours worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')
print('---------------------------------------------------------------------------')
print(f'{hours_worked:<15} {Pay_Rate:<12.2f} {Over_Time:<11} {Overtime_pay:<9.2f} {RegHour_pay:<15.2f} {Gross_pay:<15.2f}')



