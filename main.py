# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbraCins.com/help/pycharm/
from random import randint
from decouple import config

money = config('MY_MONEY')
print(f' you have {money}')
play = input('do you wanna play? (yes or no)')
bet = int(input('your bet:'))
while play.strip().lower() == 'yes':
    num = randint(1, 30)
    guess = input('guess high or low than 16')
    if guess.strip().lower() == 'high':
        if num > 15:
            print(f'you guessed correctly! the number was {num}')
            money = money + bet * 2
            print(f'you have {money}')
            play = input('do you wanna play? (yes or no)')
            if money < 1:
                print('time to top your balance')
                break
    else:
        print('high or low')
        if num < 16:
            print(f'you guessed wrong! the number was {num}')
            money = money - bet * 2
            print(f'you have {money}')
            play = input('play again?(yes or no)')
            if money < 1:
                print('time to top your balance')
                break
    if guess.strip().lower() == 'low':
        if num < 16:
            print(f'you guessed correctly! the number was {num}')
            money = money + bet * 2
            print(f'you have {money}')
            play = input('do you wanna play? (yes or no)')
            if money < 1:
                print('time to top your balance')
                break
        if num > 15:
            print(f'you guessed wrong! the number was {num}')
            money = money - bet * 2
            print(f'you have {money}')
            play = input('play again?(yes or no)')
            if money < 1:
                print('time to top your balance')
                break

