'''file that will do 4 basic operations'''

def add(x,y):
  print(str(x + y) + '\n')
  return(x+y)

def subtract(x,y):
  print(str(x - y) + '\n')
  return(x-y)

def multiply(x,y):
  print(str(x * y) + '\n')
  return(x*y)

def divide(x,y):
  print(str(x / y) + '\n')
  return(x/y)

value = 10
def practice_with_global_variable():
  #global value 
  value = value + 30
  print(value)
