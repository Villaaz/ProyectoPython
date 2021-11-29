import random

def fifty_fifty():
    return random.randrange(2)

print('\nWelcome to the Coin Toss App')
times = int(input('\nI will flip a coin a set number of times.\nHow many times would you like me to flip the coin: '))
seeResult = input('Would you like to see the result of each flip (y/n): ').lower()
heads = 0
tails = 0
print('\nFlipping!!!')
for i in range(times):
    if seeResult[0] == 'y':
        result = fifty_fifty()
        if result == 0:
            print('TAILS')
            tails += 1
            if tails == heads:
                print(f'At {tails+heads} flips, the number of heads and tails were equal at {tails} each.')
        elif result == 1:
            print('HEADS')
            heads += 1
            if tails == heads:
                print(f'At {tails+heads} flips, the number of heads and tails were equal at {tails} each.')
    elif seeResult[0] == 'n':
        result = fifty_fifty()
        if result == 0:
            tails += 1
            if tails == heads:
                print(f'At {tails+heads} flips, the number of heads and tails were equal at {tails} each.')
        elif result == 1:
            heads += 1
            if tails == heads:
                print(f'At {tails+heads} flips, the number of heads and tails were equal at {tails} each.')
    else:
        print('\nPlease input a valid order.')
print('\nResults Of Flipping A Coin {times} Times:')
porcHeads = round((heads/(heads+tails))*100)
porcTails = round((tails/(heads+tails))*100)
print(f'\nSide\tCount\tPercentage')
print(f'Heads\t{heads}/{heads+tails}\t{porcHeads}%')
print(f'Tails\t{tails}/{heads+tails}\t{porcTails}%')