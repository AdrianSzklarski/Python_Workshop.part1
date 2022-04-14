"""     Adrian SZKLARSKI, 04.2022r,
                Lotto:

---

    Returns:      ---
    Parameters:   ---
    Error:        ---
"""
from files import MLotto

if __name__ == '__main__':
    while True:
        try:
            print('What do you want to play? ?')
            print('Select: m - lotto, d - duży lotek, l - multilotek: ', end=' ')
            selection = input(' ')

            if 'm' == selection:
                MLotto.mlotto()

            break
        except NameError:
            print("wrong choice")