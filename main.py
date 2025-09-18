import gameset
balance = 5000
end = ''
retry = ['Y', 'y', 'yes']

while True:
    bet = gameset.betting(balance)
    balance -= bet

    print(f'You betted ${bet}')
    print(f'Your balance is ${balance}')

    balance += gameset.dice_roll(bet)

    if balance < 1:
        print("You're out of money.")
        end = input('You lose! Retry? ')
        if end in retry:
            total = 1000
            continue
        else:
            break

    print(f'Your balance is ${balance}')
