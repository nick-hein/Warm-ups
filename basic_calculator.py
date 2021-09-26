'''
This warm-up is meant as a preview/overview of the skills learned in section 1.2

Skills covered:
- function/procedure
  - parameters
  - arguments
  - global variables
- abstraction
- storing data in a list vs text file
- list indexing
- list manipulation methods (append,pop,insert,remove)
- opening a file, read vs write
- recording a name/word
'''

#import python module with basic algorithms
import four_operations as operation

#keep track of calculations
calculation_history = []

#while loop that will ask user for 2 inputs x, y
while True:
  #take input from user
  print('\n','Selection operation: ')
  print("1. Add")
  print("2. Subract")
  print("3. Multiply")
  print("4. Divide")
  choice = input("Enter choice 1/2/3/4: ")
  first_number = int(input('Provide first number: '))
  second_number = int(input('Provide second number: '))
  if choice == '1':
    calculation_history.append(operation.add(first_number, second_number)) #add their output to calculation_history
  elif choice == '2':
    calculation_history.append(operation.subtract(first_number, second_number))
  elif choice == '3':
    calculation_history.append(operation.multiply(first_number, second_number))
  elif choice == '4':
    calculation_history.append(operation.divide(first_number, second_number))
  
  #if done, break loop
  finished = input('Do you want to do another calculation? (y/n) ')
  if finished == 'n':
    break

#add to a text file that records outputs
file = open('four_operations_history.txt','w') #this mode opens the file and erases its contents for a fresh start

track_calculation_history = 0
while track_calculation_history < len(calculation_history):
  file.write(str(calculation_history[track_calculation_history]))
  track_calculation_history += 1

file.close()