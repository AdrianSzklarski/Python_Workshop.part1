import random

DICES = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")
Points = 0


def player(dices):

    array = []
    for i in range(1, 3):
        while True:
            play = input('Choose dice from DICES list: ').upper()
            if play in dices:
                array.append(play)
                array.sort()
                i += 1
                break
            else:
                print('Wrong Value!, Try again')
    return array


def computer():

    array = []
    for i in range(1, 3):
        array.append(random.choice(DICES))
        array.sort()
        i += 1
    return array


def resume():
    pass

chosse_play = player(DICES)
print(chosse_play)
chosse_comp = computer()
print(chosse_comp)
resume()
