import random

while True:
    try:
        scope_of_min_numbers = int(input('Specify a range minimum of numbers: '))
        scope_of_max_numbers = int(input('Specify a range maximum of numbers: '))
        break
    except ValueError or NameError:
        print("You should have given either an int")


def Guess_the_numberC(scope_of_min_numbers, scope_of_max_numbers):
    draw = random.randint(scope_of_min_numbers, scope_of_max_numbers)
    print('the number drawn was: ', draw)


Guess_the_numberC(scope_of_min_numbers, scope_of_max_numbers)