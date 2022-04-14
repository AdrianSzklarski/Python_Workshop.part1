import random


def mlotto():

    array = []
    while True:
        try:
            numbers = int(input('Give five numbers from 1 - 42: '))
            if numbers not in array and numbers <= 42 and numbers >= 1:
                array.append(numbers)
                array.sort()
                if len(array) > 4:
                    print(f'The user selected the following numbers {array}')
                    break
            else:
                print('Wrong Value, try again')
        except ValueError:
            print("You should have given either an int")


if __name__ == '__main__':
    mlotto()
