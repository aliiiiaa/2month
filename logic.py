import random
import time


def bet(b, g):
    print("wait...")
    time.sleep(2)
    choice = random.randint(1, 31)
    if choice == b:
        print(choice)
        print('you won!')
        return g * 2
    else:
        print(choice)
        print(f'-{g}$')
        print('try again')

        return 0
