#!/usr/bin/python3

	"""
	Print the numbers 1-100 separated by space.
	For multiples of three, print Fizz
	For multiples of five, print Buzz
	For multiples of three and five, print FizzBuzz
	"""


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
