'''
week 5 warm-up

skills covered:
procedures/functions with an algorithm containing sequence, selection, and iteration
random module
'''
'''
week 5 warm-up

skills covered:
- procedures/functions with an algorithm containing sequence, selection, and iteration
- test cases with procedure
- random module
'''
#Super Lotto Plus number generator

import random as rand


previous_picks = []
repeat_picks = []


def Super_Lotto_Plus(how_many_numbers, mega_number):
  global previous_picks
  global repeat_pick
  print('Let me generate some numbers for you' + '\n')
  for i in range(1, how_many_numbers + 1):
    pick = rand.randint(1,47)
    repeat = True
    while repeat:
      if pick in previous_picks:
        pick = rand.randint(1,47)
        repeat_picks.append(pick)
      else:
        break
    previous_picks.append(pick)
    print('Pick ', str(i), ': ', pick)
  if mega_number == 'y':
    mega_number_pick = rand.randint(1,27)
    print('Mega_number_pick: ', str(mega_number_pick))
  else:
    print('Mega_number_not_selected')
  print('Good luck and hope you win big!','\n')
  print('Numbers repeated: ', str(repeat_picks))
  print('Previous_picks: ', str(previous_picks))


Super_Lotto_Plus(5,'n')
#Super_Lotto_Plus(5,'y')
