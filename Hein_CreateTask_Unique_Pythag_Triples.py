10#create an open list to store pythag triples
unique_triple = []
duplicates = []
legs_reversed = []
multiples = []

#pythagorean theorem
def pythag(a,b,c):
  if a**2 + b**2 == c**2:
    return True
  else:
    pass

#loop to check for pythag triples
def pythag_triples(number,numbers_to_check):
  count = 0
  number = input('How many pythagorean triples do you want to find?' + '\n')
  numbers_to_check = int(input('What range of numbers do you want to search in?' + '\n'))
  for a in range(1,numbers_to_check + 1): #add 1 to make sure range is inclusive
    for b in range(1,numbers_to_check + 1):
      for c in range (1,numbers_to_check + 1):
        if pythag(a,b,c) == True:
          if count == 0: #first pythag triple to add to list
            unique_triple.append([a,b,c])
            count += 1
          else: 
            avoid = 0 #set a new counter 
            for elements_in_each_pythag_triple in unique_triple: #add to counter if it is one of the following:
              if [a,b,c] in unique_triple: #repeats of same
                duplicates.append([a,b,c])
                avoid += 1
                break
              elif [b,a,c] in unique_triple: #repeats of pythag triples with reversed legs a,b
                legs_reversed.append([a,b,c])
                avoid += 1
                break
              elif elements_in_each_pythag_triple[0] / a == elements_in_each_pythag_triple[1] / b == elements_in_each_pythag_triple[2] / c: #multiples of pythag triples
                multiples.append([a,b,c])
                avoid += 1
                break
              elif elements_in_each_pythag_triple[1] / a == elements_in_each_pythag_triple[0] / b == elements_in_each_pythag_triple[2] / c: #multiples of reveresed legs a,b pythag triples
                multiples.append([a,b,c])
                avoid += 1
                break
            if avoid != 1: #if it did not add to counter from any of the above conditions, then add to unique list
              unique_triple.append([a,b,c])
              count += 1
        else:
          pass
        if count == int(number):
          break
  
  #output range chosen
  print ('\n'+ 'Range of numbers checked inclusive: [0, ' + str(numbers_to_check) + ']'+ '\n')

  #output if count of numbers they want is less than what they are
  if int(count) < int(number):
    print('Unfortunately, there were only ' + str(count) + ' unique pythagorean triples' + '\n')

  #output
  print ('The first ' +str(count) + ' unique pythagorean triples are:' + '\n')
  print (*unique_triple, sep=' \n')
  print ('\n')

pythag_triples(1,2)