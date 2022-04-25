"""     Adrian SZKLARSKI, 04.2022r,
        A game of guessing numbers:

2001 - Rules of the Game Each player starts with 0 points. In his turn,
a player rolls 2 dice (standard hex dice). The number of eyes thrown is
added to the total points. Starting on the second turn: if the player throws
a 7, he divides his number of points by this value discarding the fractional
part, if he throws 11, he multiplies his current number of points by this value.
The player who first reaches 2001 points wins.

    Returns:      numbers drawn during the game and who won the game
                  (first to score 2001 points)

    Parameters:   value from two dice drawn by the player and the computer

    Error:        ValueError or NameError
"""

import random
import time

DICES = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")


def player(dices):
    array_p = []
    for i in range(1, 3):
        while True:
            play = input('Choose dice from DICES list: ').upper()
            if play in dices:
                array_p.append(play)
                array_p.sort()
                i += 1
                break
            else:
                print('Wrong Value!, Try again')
    return array_p


def computer():
    array_c = []
    for i in range(1, 3):
        array_c.append(random.choice(DICES))
        array_c.sort()
        i += 1
    return array_c


def game(cp, cc):
    print(f'The player has selected the dice {cp}')
    print(f'The computer has drawn dice      {cc}')

    cp_first_throw = cp[0][1:]
    cp_second_throw = cp[1][1:]
    cc_first_throw = cc[0][1:]
    cc_second_throw = cc[1][1:]

    points_player = 0
    sum_array_player = 0
    array_player = []

    points_comp = 0
    sum_array_comp = 0
    array_comp = []

    first_points_player = random.randint(1, int(cp_first_throw)) + \
                          random.randint(1, int(cp_second_throw))
    first_points_computer = random.randint(1, int(cc_first_throw)) + \
                            random.randint(1, int(cc_second_throw))

    while (sum_array_player + first_points_player) < 2001 and (sum_array_comp + first_points_computer) < 2001:

        input('Push Enter: ')
        roll_player = random.randint(1, int(cp_first_throw)) + \
                      random.randint(1, int(cp_second_throw))
        roll_computer = random.randint(1, int(cc_first_throw)) + \
                        random.randint(1, int(cc_second_throw))

        if roll_player == 7:
            points_player //= 7
            array_player.append(points_player)
        elif roll_player == 11:
            points_player = 11
            array_player.append(points_player)
        else:
            points_player = roll_player
            array_player.append(points_player)
        sum_array_player = sum(array_player)
        print(f'Sum Player points: {sum_array_player}')
        time.sleep(0.5)

        if roll_computer == 7:
            points_comp //= 7
            array_comp.append(points_comp)
        elif roll_computer == 11:
            points_comp = 11
            array_comp.append(points_comp)
        else:
            points_comp = roll_computer
            array_comp.append(points_comp)
        sum_array_comp = sum(array_comp)
        print(f'Sum Computer points: {sum_array_comp}')

    return (sum(array_player) + first_points_player), (sum(array_comp) + first_points_computer)


if __name__ == '__main__':
    print('Choose your dice: ', DICES)
    chosse_play = player(DICES)
    chosse_comp = computer()
    res = game(chosse_play, chosse_comp)
    if res[0] > 2001:
        print('Player is VIN!')
    elif res[1]:
        print('Computer is VIN!')
    else:
        print('There is no winner!')
