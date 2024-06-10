def calculate_score(finaid, age):
  """ Calculates score based on answers given to questions.
  >>> calculate_score("yes", 10)
  10
  >>> calculate_score("no", 10)
  0   
  """

  # YOUR CODE HERE
# If the student recieves finacial aid award 10 points, validate that the answer is yes or no
  while True:
      finaid = input('Do you receive Finacial Aid? Yes / No: ')
      if finaid.capitalize() == 'Yes':
          score =+ 10
          print('The user typed in Yes')
          break
      elif finaid.capitalize() == 'No':
          score =+ 0
          print('The user typed in No')
          break
      else:
          print('Enter Yes or No')
          continue    
  print ("Financial Aid points awarded? ", score)
    
# Collect the student's current age and validate input value is an integer, 
# awared points based on results, under 19 years of age are awarded points.
  while True:
      try:
         age = int(input( "How old are you? " ))
      except ValueError:
         print("Not an integer! Try again.")
         continue
      else:
         break 

  if age < 19:
       score =+ 10
  elif age > 19:
       score =+ 0
  print ('Age points awarded', score)    

# Total up the points based on input variables
 
  print ("Total points awarded = ", score)
  return score  


  
# This code runs the doctests to see if they pass/fail
import doctest
doctest.run_docstring_examples(calculate_score, globals(),
    verbose=True, name="calculate_score")