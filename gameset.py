import random

def is_integer(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

def betting(maxint):
    put_in = input('How much would you like to bet? ')
    while True:
        while is_integer(put_in):
            if int(put_in) >= maxint:
                print('All in!')
                return maxint
            else:
                return int(put_in)
        if put_in == 'all in':
            print('All in!')
            return maxint
        else:
            print('Must bet an integer or "all in"')
            continue

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