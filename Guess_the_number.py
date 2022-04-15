"""     Adrian SZKLARSKI, 04.2022r,
        A game of guessing numbers:

A game of guessing numbers from 1 to 100 in ten moves

    Returns:      numbers drawn during the game
    Parameters:   the value of the number in the case of a player
                  or the result of a draw for a computer
    Error:        ValueError or NameError
"""
from files import Gtn_Computer, Gtn_Player

if __name__ == '__main__':
    while True:
        try:
            print('Do you want to play, or should the computer play?')
            print('Select: You - y, Computer - c: ', end=' ')
            selection = input(' ')

            if 'c' == selection:
                Gtn_Computer.guess_the_numberC()

            if 'y' == selection:
                Gtn_Player.guess_the_numberC()

            break
        except NameError:
            print("Wrong choice, try agian")


