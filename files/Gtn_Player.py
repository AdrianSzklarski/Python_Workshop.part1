import random

def guess_the_numberC():

    my_number_is = random.randint(0, 100)

    while True:
        try:
            count = int(input('give a number in the range: '))
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
