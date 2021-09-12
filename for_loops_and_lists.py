'''
Week 3 warm-up: What to wear today?

Questions:
1. Describe purpose of code? (What it does)
2. Describe functionality of code? (How it works)
3. Describe input and output
4. Why does the code require 'str' in lines 21 and 22?
5. Describe the block of code from lines 25 - 34?
6. Explain how the nested for loops work in last block of code.
'''

#list of possible tops
tops = ['white t-shirt', 'black t-shirt', ' blue polo', 'tank top', 'dress shirt']

#list of possible bottoms
bottoms = ['light blue jeans','dark blue jeans', 'white shorts', 'gray shorts', 'sweatpants']

#print current tops and bottoms
print('Here are your current tops and bottoms:')
print('tops: ' + str(tops))
print('bottoms: ' + str(bottoms) + '\n')

#ask user if they have any more clothes
additional_clothes = input('Do you have any more clothes? (y/n) ')
if additional_clothes == 'y':
  
  what_type = input('Is it a top or a bottom? ')
  if what_type == 'top':
    additional_top = input('Describe what it is? ')
    tops.append(additional_top)
  else:
    additional_bottom = input('Describe what it is? ')
    bottoms.append(additional_bottom)

#print new combinations
print('Here are all your possible combinations:')
for i in tops:
  for j in bottoms:
    print(i + '-' + j)


