from files.Gtn_Player import Guess_the_numberP
from files.Gtn_Computer import Guess_the_numberC

# 1a. Jeżeli gra komputer, użytkownik musi zdeklarować liczbę;
# 1b. W ciągu 10 ruchów użytkownik podaje komputerowi czy wylosował za dużo czy za mało;
# 2a. Jeżeli gra użytkownik pojawia się komunikat "za dużo", "za mało", "wygrałeś", "podana liczba jest poza zakresem";
# 3. W każdym przypadku program ma obsłużyć możliwe błędy gry;
# 4. Gra ma być zaimpelmentowana we Flasku



if __name__ == '__main__':
    while True:
        try:
            print('Do you want to play, or should the computer play?')
            print('Select: You - y, Computer - c: ', end=' ')
            selection = input(' ')

            if 'y' == selection:
                Guess_the_numberP()
            if 'c' == selection: # letter c
                Guess_the_numberC()
            break
        except NameError:
            print("wrong choice")


