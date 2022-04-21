import random

DICES = ('D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100')
Points = 0


def player():
    pass


def computer():

    array = []
    for i in range(1, 3):
        array.append(random.choice(DICES))
        i += 1
    return array


def resume():
    pass


player()
chosse_comp = computer()
print(chosse_comp)
resume()
