import random

DICES = ("D100", "D20", "D12", "D10", "D8", "D6", "D4", "D3")  # Declarations
SINGS = ("+", "-", "")
type_of_dice = random.choice(DICES)


def game_of_dice(TypeDices):
    """
    Calculate dice roll from dice pattern.

    :param str dice_code: dice pattern ex.`7D12-5`

    :return: dice roll value for proper dice pattern, `Wrong Input` text elsewhere
    """

    for _ in TypeDices:

        div = TypeDices.split(' ')

        for i in div:  # Checking the mark and occurrences of the letter D
            finded = i.find('D')
            findedp = i.find('+')
            findedm = i.find('-')
            are = i.count('D')

            try:
                if '+' in i: # Conditions for marks
                    plus = int(i[findedp + 1:])
                    return plus
                elif '-' in i:
                    minus = int(i[findedm + 1:])
                    return minus
            except ValueError:
                pass

            if are == 1: # Breakdown of text
                if finded > 0:
                    multiply = i[:finded]
                    try:
                        multiply = int(multiply)
                    except ValueError:
                        return f'Wrong value! {multiply}'
                else:
                    multiply = 1
            else:
                return f'Wrong value, You have more than one D = {are}!'

        return multiply


def random_of_dice(): # Drawing and display of the drawn dice

    number_of_throws = str(random.randint(1, 5))
    sings_of_dice = random.choice(SINGS)
    modifier = str(random.randint(1, 10))
    TypeDices = number_of_throws + type_of_dice + sings_of_dice + modifier
    print(f'A dice was drawn: {TypeDices}')
    print(f'Number_of_throws: {number_of_throws}, Modifier: {modifier}')

    resume = " "
    if len(resume) < random.randint(1, 9): # Limitation of the number of characters
        return int(number_of_throws), int(modifier)


def throws(tod, array): # Dice rolls

    div = int(tod[1:])
    suma = []
    number_of = array[0]
    for i in range(1, number_of + 1):
        suma.append(array[0] * random.randint(1, div)) # Mathematical formula: xDyy+zz
    return f'Results of throws : {suma}', f'Sum results of throws {sum(suma)+array[1]}'

if __name__ == '__main__':
    try:
        rfd = random_of_dice()
        god = game_of_dice(str(rfd))
        su = throws(type_of_dice, rfd)
        print(su)
    except TypeError:
        print(f'Wrong value!')
