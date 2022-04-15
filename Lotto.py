"""     Adrian SZKLARSKI, 04.2022r,
                Lotto:

    Returns:      drawing 5 numbers out of 42,
    Parameters:   5 numbers int,
    Error:        NameError and ValueError.
"""
from files import MLotto


if __name__ == '__main__':

    while True:

        print('What do you want to play? ?')
        print('Select: l- lotto to start, n - exit:', end='')

        selection = input(' ')
        if 'l' == selection:
            new_mlotto = MLotto.mlotto()
            print(f'The user selected the following numbers:  ', new_mlotto)
            new_clotto = MLotto.clotto()
            print(f'The lotto selected the following numbers: ', new_clotto)
            print(f'Improved numbers : ', MLotto.resume(new_mlotto, new_clotto))
            break
        elif 'n' == selection:
            exit()
        else:
            print(f'Wrong choice, try again')




