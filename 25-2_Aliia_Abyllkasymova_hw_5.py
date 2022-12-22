from decouple import config
from logic import bet

My_Money = int(config('MY_MONEY'))
while True:
    print('you have ' + str(My_Money))
    print('do you wanna play? (yes or no)')
    a = input('')
    if a.strip() == 'no':
        print('you are out of the game')
        break
    elif a.strip() == 'yes':
        b = int(input('guess the number from 1 to 30 '))
        g = int(input('your bet '))
        My_Money -= g
        My_Money += bet(b, g)

    else:
        print('yes or no')
