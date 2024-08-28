'''
114 While loops and modulus warm-up
Times when the train comes by the house

Questions:
1. What does line 12 do? What line do we use it in?
2. What is the while loop doing?
3. Explain line 25 and its purpose in this code.
4. How many variables are used? What are the variables used in this code?
'''

import random

#each day of the week
day_of_the_week = 0

#time of the day
am_time = 0
pm_time = 0

#record time of the train each day
while day_of_the_week <= 6:
  train_time = random.randint(0,25)
  if train_time >= 12:
    pm_time = train_time % 12
    print(str(pm_time) + 'pm')
  else:
    am_time = train_time
    print(str(am_time) + 'am')
  day_of_the_week += 1