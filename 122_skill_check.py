'''
122_skill_check on functions and indexes
Answer the questions below. Ask as necessary

1. How many functions/procedures are in this code?
2. How many parameters does the first function have? What is the name of the parameter?
3. On what lines are the functions called?
4. What is the name of the argument used to call the function?

5. The code creates a variable minimum = lst[0]. What is lst[0]?
6. How does the following block work?
      for i in range(len(lst)):
        if lst[i] < minimum:
          minimum = lst[i]

7. Are there any lines of code you do not understand?
'''


#generate list of 10 random numbers from 0 to 100
import random
numbers = []
for i in range(10):
  numbers.append(random.randint(0,100000))

#functions to determine minimum or maximum of a list
def min_of_list(lst):
  minimum = lst[0]
  for i in range(len(lst)):
    if lst[i] < minimum:
      minimum = lst[i]
  print(minimum,lst)

def max_of_list(lst):
  maximum = lst[0]
  for i in range(len(lst)):
    if lst[i] > maximum:
      maximum = lst[i]
  print(maximum,lst)

#ask user if they want min or max of list
user_input = input('Do you want the min or max of the list? \n')
while user_input != 'min' and user_input != 'max':
  user_input = input('You inputted something different than min or max. Please select min or max \n')

if user_input == 'min':
  min_of_list(numbers)

elif user_input == 'max':
  max_of_list(numbers)




