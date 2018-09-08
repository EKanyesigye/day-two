#!/usr/bin/python
def fizz_buzz(argument):
    """
        This function returns 'Fizz', 'Buzz', 'FizzBuzz', If the function is divisible by 3, it will return fizz,if it is is divisible by 5, it will return buzz, and if divisible by both 3 and 5 then will return fizzbuzz . 
    """

 

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

