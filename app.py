'''
Main file for running the application. It imports and uses the functions from
functions.py file to prompt the user for a natural number and checks if it is
multiple of 7, 5 or neither of them.
'''

from functions import get_natural, multiple_five, multiple_seven, if_not_multiple_seven_and_five


number = get_natural()
print(multiple_five(number) + multiple_seven(number) +
      if_not_multiple_seven_and_five(number))
