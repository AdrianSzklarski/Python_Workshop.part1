import random
from files.Gtn_Player import Gtn_Player
from files.Gtn_Computer import Gtn_Computer

# 1.  Użytkownik ma zadeklarować czy zgaduje on, czy komputer
# 1a. Jeżeli gra komputer, użytkownik musi zdeklarować liczbę;
# 1b. W ciągu 10 ruchów użytkownik podaje komputerowi czy wylosował za dużo czy za mało;
# 2a. Jeżeli gra użytkownik pojawia się komunikat "za dużo", "za mało", "wygrałeś", "podana liczba jest poza zakresem";
# 3. W każdym przypadku program ma obsłużyć możliwe błędy gry;
# 4. Gra ma być zaimpelmentowana we Flasku

def Guess_the_number(scope_of_min_numbers, scope_of_max_numbers):
    draw = random.randint(scope_of_min_numbers, scope_of_max_numbers)
    print('the number drawn was: ', draw)


if __name__ == '__main__':
    while True:
        try:
            scope_of_min_numbers = int(input('Specify a range minimum of numbers: '))
            scope_of_max_numbers = int(input('Specify a range maximum of numbers: '))
            break
        except ValueError or NameError:
            print("You should have given either an int")

    while True:
        try:
            print('Do you want to play, or should the computer play?')
            print('Select: You - y, Computer - c: ', end=' ')
            selection = input(' ')

            if 'y' == selection:
                Gtn_Player()
            if 'c' == selection: # letter c
                Gtn_Computer()
            break
        except NameError:
            print("wrong choice")


Guess_the_number(scope_of_min_numbers, scope_of_max_numbers)