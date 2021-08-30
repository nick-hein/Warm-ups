'''
Multiplying numbers with nested while loops

Questions:
1. What does this code do?
2. How does this code work?
3. Explain how the block from 14-16 works?
4. Explain how the nested while loop works?
5. Why does multipliers_up_to_set_number need to be redefined to 1 again in line 30?
'''

#ask user for number
user_number = input('What number do you want to know the multiplication table up to? ')

#check if it is an integer greater than 1
while float(user_number) < 1 or '.' in user_number:
  user_number = input('Must be an integer greater than 0. \nWhat number do you want to know its factors if? \n')

#variables for where to start multiplying and what to multiply up to
starting_number = 1
multipliers_up_to_set_number = 1
set_number = 10

#multiply each number from 1 up to set number for all numbers up to user number
while starting_number <= int(user_number):
  while multipliers_up_to_set_number <= set_number:
    print(str(starting_number), 'x', str(multipliers_up_to_set_number), '=',  starting_number * multipliers_up_to_set_number)
    multipliers_up_to_set_number +=1
  multipliers_up_to_set_number = 1  
  starting_number += 1
