import random

def guess_the_numberC():

    my_number_is = random.randint(0, 100)      # the computer draws its number

    while True:
        try:
            count = int(input('Give the number you are looking for [1 - 100] : '))
            if count > my_number_is:
                print('you have given too high a value, try again')
            elif count < my_number_is:
                print('you specified too small a value , try again')
            else:
                print('You WIN! :D')
                break
        except Exception:
            print("You should have given either an int")

if __name__ == '__main__':
    guess_the_numberC()
