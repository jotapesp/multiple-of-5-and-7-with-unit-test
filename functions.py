'''
This module contains all the functions to determine if a number
is multiple of 5 or multiple of 7 or if not multiple of any of
them.
'''


def multiple_five(number):
    '''
    Check if number is multiple of 5 and return 'fizz' if True
    '''
    if number % 5 == 0:
        return 'fizz'
    return ''

def multiple_seven(number):
    '''
    Check if number is multiple of 7 and return 'buzz' if True
    '''
    if number % 7 == 0:
        return 'buzz'
    return ''

def if_not_multiple_seven_and_five(number):
    '''
    Check if number is not multiple of 5 and 7 at the same time, returning
    "miss" if True
    '''
    if multiple_five(number) == '' and multiple_seven(number) == '':
        return 'miss'
    return ''

def get_natural():
    '''
    Prompts the user to input a Natural number, returning ValueError case
    the input is not a Natural number or the input itself in case it is.
    '''
    while True:
        try:
            number = int(input("Insert a natural number: "))
            if not isinstance(number, int):
                raise ValueError("Natural numbers should be integer values")
            if number < 0:
                raise ValueError("Negative numbers do not belong to Natural")
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return number
