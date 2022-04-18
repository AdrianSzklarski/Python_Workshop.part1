import random

DICES = ("D100", "D20", "D12", "D10", "D8", "D6", "D4", "D3") # Possible dices types

def game_of_dice(TypeDices):
    """
    Calculate dice roll from dice pattern.

    :param str dice_code: dice pattern ex. `7D12-5`

    :rtype: int, str
    :return: dice roll value for proper dice pattern, `Wrong Input` text elsewhere
    """


    for _ in TypeDices:

        TypeDices_lenght = len(TypeDices)  # Length of type dices
        div = TypeDices.split(' ')  # Breakdown into array

        for i in div:  # Checking on which index the  D, +, -
            finded = i.find('D')
            findedp = i.find('+')
            findedm = i.find('-')

        if finded > 0:  # If index D > 0
            multiply = i[:finded]  # Cutting from 0 to index-1
            try:
                multiply = int(multiply)  # Converted to 'int'
            except ValueError:
                return f'Wrong value! {multiply}'
        else:
            multiply = i[0]  # D on index 0

        return multiply


if __name__ == '__main__':
    print(game_of_dice("5D10+10"))
    print(game_of_dice("D6"))
    print(game_of_dice("2D3"))
    print(game_of_dice("D12-1"))
    print(game_of_dice("DD34"))
    print(game_of_dice("4-3D6"))

