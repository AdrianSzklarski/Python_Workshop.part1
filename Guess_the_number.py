from files import Gtn_Computer, Gtn_Player

# 1a. Jeżeli gra komputer, użytkownik musi zdeklarować liczbę;
# 1b. W ciągu 10 ruchów użytkownik podaje komputerowi czy wylosował za dużo czy za mało;
# 3. W każdym przypadku program ma obsłużyć możliwe błędy gry;
# 4. Gra ma być zaimpelmentowana we Flasku

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


