# CTI-110

# P2HW2 - List

# Benjamin Leal

# 10/6/23

#Grade statement

mod_1 = float(input('Enter grades for module 1:'))
mod_2 = float(input('Enter grades for module 2:'))
mod_3 = float(input('Enter grades for module 3:'))
mod_4 = float(input('Enter grades for module 4:'))
mod_5 = float(input('Enter grades for module 5:'))
mod_6 = float(input('Enter grades for module 6:'))

# List
grades = [mod_1,mod_2,mod_3,mod_4,mod_5,mod_6]

#Grades

low = min(grades)
high = max(grades)
total = sum(grades)
avg = sum(grades) / len(grades)

# Results

print('--------------- Results ----------------')

print('Lowest Grade:',min(grades))
print('Highest Grade:',max(grades))
print('Sum of grades:',sum(grades))
print('Average:',sum(grades) / len(grades))
 
