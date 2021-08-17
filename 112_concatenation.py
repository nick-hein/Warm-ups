'''
1.1.2 Concatenation and Data Type Warm-up

Answer the following questions:
1. What does this code do?
2. How many variables are in this code? What are they named?
'''

#Get user information
print('\nWelcome \n')
user_name = input('What is your name? ')
user_age = input('What is your age? ')
print('Welcome ', user_name, '!', 'You said you are of the age', user_age, '\n')

#Get parent information
parents_age = input('How old is one of your parents? ')

#Calculate difference between ages
difference = parents_age - user_age
print('There is a difference of ' + difference + ' years between you two \n')