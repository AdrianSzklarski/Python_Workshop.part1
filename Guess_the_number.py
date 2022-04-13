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
            print("wrong choice")


