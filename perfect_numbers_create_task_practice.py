'''
Calculate perfect numbers. A perfect number is a number where all
its factors also sum to that number. Example: 6. Factors 1,2,3. 
1+2+3 = 6

1. What is the name of the function?
2. What is the name of the parameter? 
3. What is the name of the argument used in the function?
4. Does the argument cause 2 different blocks of code to run? Explain.
5. Is there iteration and selection in the function?
6. Where do I add data to my list?
7. How do I use my list?
'''
perfect_numbers = []

def perfect_number(range_of_numbers):
  global perfect_numbers
  while (range_of_numbers) >= 10000:
    range_of_numbers = int(input('Number must be less than 10000. Please provide a new number '))
  for i in range(1,range_of_numbers):
    #calculate factors of the number
    factors = []
    for j in range(1,i):
      if i % j == 0:
        factors.append(j)
    #check if the factors sum to that number
    sum_of_factors = 0
    for k in factors:
      sum_of_factors += k
    if sum_of_factors == i:
      perfect_numbers.append(i)
  print (perfect_numbers)
  return perfect_numbers

user_input = int(input('Provide a number that is less than 10000. '))
perfect_number(user_input)

follow_up_question = int(input('How many perfect numbers do you think were found? '))
if follow_up_question == len(perfect_numbers):
  print('You are correct. There were', str(len(perfect_numbers)), 'perfect numbers. They were: \n',str(perfect_numbers))
else:
  print('You are not correct. There were', str(len(perfect_numbers)), 'perfect numbers. They were: \n',str(perfect_numbers))
