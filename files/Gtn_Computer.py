def guess_the_numberC():

    max = 100
    min = 1

    print('After guess choice: You guessed it "b", too big; it "s", too small; it "v", You Win!')

    while True:

        try:
            scope_of_min_numbers = int(input('Give the number you are looking for [1 -100]: '))  # the user chooses a number to play
            if scope_of_min_numbers >=1 and scope_of_min_numbers <=100:
                break
            else:
                print('You gave the wrong value, try again')
        except ValueError:
            print("You should have given either an int")

    while True:

        guess = int((max - min) // 2 + min)  # Value drawn by the computer
        print(f'Your number is: {scope_of_min_numbers} but my number is {guess}, Did I guess?', end=' ')
        result = input(': ')

        if 'b' == result:
            max = guess

        elif 's' == result:
            min = guess

        elif 'v' == result:
            print('You WIN!')
            break
        else:
            print('You gave the wrong value, try again')

if __name__ == '__main__':
    guess_the_numberC()

