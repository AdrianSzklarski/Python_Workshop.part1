import random

def guess_the_numberC():

    while True:
        try:
            scope_of_min_numbers = int(input('Specify a range minimum of numbers: '))
            scope_of_max_numbers = int(input('Specify a range maximum of numbers: '))

            if scope_of_min_numbers < scope_of_max_numbers or scope_of_min_numbers == scope_of_max_numbers:
                draw = random.randint(scope_of_min_numbers, scope_of_max_numbers)
                print('the number drawn was: ', draw)
                break
            else:
                print("You have specified the wrong range of values, try agian ")

        except ValueError or NameError:
            print("You should have given either an int")

if __name__ == '__main__':
    guess_the_numberC()
