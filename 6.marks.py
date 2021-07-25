print ('Enter percentage of subjects to check pass or fail.')

a= int (input('Enter math percentage : '))
b= int (input('Enter chemistry percentage : '))
c= int (input('Enter physics percentage : '))

sum = float((a+b+c)/3)
if (a>33):
    print("You have passed in math.")
else:
    print("You have failed in math.")    
if (b>33):
    print("You have passed in chemistry.")
else:
    print("You have failed in chemistry.")     
if (c>33):
    print("You have passed in physics.")
else:
    print("You have failed in physics.")

print('''If you fail in any of subject you have to give the exams again although if you have
passed in overall percentage.''')
print("Let's check you have passed in overall or not.")

if (sum > 40):
    print("You have passed in overall with ", sum ," percentage.")
else:
    print('You have failed in overall with ', sum ,'percentage.')
