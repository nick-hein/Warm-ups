'''
Determine all factors of a number

Questions:
1. What is the purpose of this code?
2. How does this code work?
3. Explain how the block from 14-16 works?
4. In line 23, why does the range go from 1 to int(user_number) + 1?
5. Why is str needed  in front of factors in line 28?

'''

#ask user for number
user_number = input('What number do you want to know its factors of? ')

#check if it is an integer greater than 1
while float(user_number) < 1 or '.' in user_number:
  user_number = input('Must be an integer greater than 0. \nWhat number do you want to know its factors if? \n')

#list to keep factors
factors = []

#check each number from 1 up to user number to see if it is a factor
for iteration in range(1, int(user_number)+1):
  if int(user_number) % iteration == 0:
    factors.append(iteration)

print('The factors of ', user_number, 'are ', str(factors))

