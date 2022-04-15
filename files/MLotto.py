import random

WIN_5 = 100000

WIN_4 = 10000

WIN_3 = 1000

FIVE_MATCH = 5

FOURTH_MATCH = 4

THREE_MATCH = 3


def mlotto():
    array = []  # Player numbers
    while True:
        try:
            numbers = int(input('Give five numbers from 1 - 42: '))
            if numbers not in array and 42 >= numbers >= 1:
                array.append(numbers)
                array.sort()
                if len(array) > 4:
                    break
            else:
                print('Wrong Value, try again')
        except ValueError:
            print("You should have given either an int")
    return array


def clotto():  # Computer numbers

    array_comp = []
    while len(array_comp) < 5:
        compNumber = random.randint(1, 42)
        if compNumber in array_comp:
            continue
        array_comp.append(compNumber)
        array_comp.sort()
    return array_comp


def resume(pleyer_array, array_computer):  # Results

    array_resume = []
    for elements in pleyer_array:
        if elements in array_computer:
            array_resume.append(elements)
            array_resume.sort()
    if len(array_resume) == THREE_MATCH:
        print(f'Congratulations you have won : ', {WIN_3}, '$ \n')
    elif len(array_resume) == FOURTH_MATCH:
        print(f'Congratulations you have won : ', {WIN_4}, '$ \n')
    elif len(array_resume) == FIVE_MATCH:
        print(f'Congratulations you have won : ', {WIN_5}, '$ \n')
    else:
        return f"Sorry, you didn't win anything this time - try again \n"
    return array_resume


if __name__ == '__main__':
    new_mlotto = mlotto()
    new_clotto = clotto()
    print(f'The user selected the following numbers:  ', new_mlotto)
    print(f'The lotto selected the following numbers: ', new_clotto)
    print(f'Improved numbers : ', resume(new_mlotto, new_clotto))
