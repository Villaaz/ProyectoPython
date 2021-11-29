import random

def random_number():
    return random.randrange(1, 21)

print('\nWelcome to the Guess My Number App')
name = input('\nHello! What is your name: ').title()
print(f'Well {name}, I am thinking of a number between 1 and 20.')
number = random_number()
x = 0

for i in range(5):
    guess = int(input('\nTake a guess: '))
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        x = 1
        break

if x == 1:
    print(f'\nGood job, {name}! You guessed my number in {i+1} guesses!')
else:
    print(f'\nGame Over. The number I was thinking of was {number}.')