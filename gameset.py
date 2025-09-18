import random

# Checks if string can be converted into integer
def is_integer(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

# Checks integer status of putin. Limits putin to a maximum of maxint. If not an integer, 'all in' is the only acceptable string.
def betting(putin, maxint):
    while True:
        while is_integer(putin):
            if int(putin) >= maxint:
                print('All in!')
                return maxint
            else:
                return int(putin)
        if putin == 'all in':
            print('All in!')
            return maxint
        else:
            return ''

# Dice roll and pot value
def dice_roll(betint):
    roll = random.randint(1,6)
    print('You rolled a ' + str(roll))
    if roll < 3:
        print(f'You lost ${betint}.')
        return 0
    elif roll == 6:
        print(f'You earned ${betint * 2}.')
        return betint * 2
    else:
        print(f'You earned ${betint + 100 * roll}.')
        return betint + 100 * roll