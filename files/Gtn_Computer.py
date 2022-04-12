import random

def guess_the_numberC():
    while True:
        try:
            scope_of_min_numbers = int(input('Specify a range minimum of numbers: '))
            scope_of_max_numbers = int(input('Specify a range maximum of numbers: '))
            break
        except ValueError or NameError:
            print("You should have given either an int")

    draw = random.randint(scope_of_min_numbers, scope_of_max_numbers)
    print('the number drawn was: ', draw)

if __name__ == '__main__':
    guess_the_numberC()