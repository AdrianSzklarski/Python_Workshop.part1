import random

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
        array_c .append(random.choice(DICES))
        array_c .sort()
        i += 1
    return array_c

def math_model(cp, cc):

    cp_first_throw = cp[0][1:]
    cp_second_throw = cp[1][1:]
    cc_first_throw = cc[0][1:]
    cc_second_throw = cc[1][1:]

    for i in range(1):
        cp_first = random.randint(1, int(cp_first_throw))
        cp_second = random.randint(1, int(cp_second_throw))
        cc_first = random.randint(1, int(cc_first_throw))
        cc_second = random.randint(1, int(cc_second_throw))
        player_sum = cp_first + cp_second
        comput_sum = cc_first + cc_second
        print(f'On the first dice, the player has thrown a number of dots:     {cp_first}\n'
              f'On the second dice, the player has thrown a number of dots:    {cp_second}\n'
              f'On the first dice, the computer threw out the number of dots:  {cc_first}\n'
              f'On the second dice, the computer threw out the number of dots: {cc_second}\n')
        print(f"The sum of the player's dots is: {player_sum}\n"
              f"The sum of the dots of the computer is: {comput_sum}\n")
        return cp_first, cp_second, cc_first, cc_second


    Points_c = 0
    Points_p = 0



def resume():
    pass

chosse_play = player(DICES)
chosse_comp = computer()
math_model(chosse_play, chosse_comp)

resume()
