import random

def random_number():
    return random.randrange(3)

moves = ['rock', 'paper', 'scissors']
print('\nWelcome to a game of Rock, Paper, Scissors')
rounds = int(input('\nHow many rounds would you like to play: '))
playerScore = 0
IAScore = 0

for i in range(rounds):
    print(f'\nRound {i+1}\nPlayer: {playerScore}\tComputer: {IAScore}')
    IAMove = random_number()
    if IAMove == 0:
        IAMove = 'rock'
    elif IAMove == 1:
        IAMove = 'paper'
    elif IAMove == 2:
        IAMove = 'scissors'
    playerMove = input(f'Time to pick...rock, paper, scissors: ').lower()
    if playerMove != 'rock' and playerMove != 'paper' and playerMove != 'scissors':
        print(f'That is not a valid game option!\nComputer gets the point!')
        IAScore += 1
    else:
        print(f'\tComputer: {IAMove}\n\tPlayer: {playerMove}')
        if playerMove == IAMove:
            print(f"\tIt is a tie, how boring!\nThis round was a tie.")
        elif playerMove == "rock":
            if IAMove == "scissors":
                print(f"\tRock smashes scissors!\nYou win round {i+1}!")
                playerScore += 1
            else:
                print(f"\tPaper covers rock! You lose round {i+1}.")
                IAScore += 1
        elif playerMove == "paper":
            if IAMove == "rock":
                print(f"\tPaper covers rock! You win round {i+1}!")
                playerScore += 1
            else:
                print(f"\tScissors cuts paper! You lose round {i+1}.")
                IAScore += 1
        elif playerMove == "scissors":
            if IAMove == "paper":
                print(f"\tScissors cuts paper! You win round {i+1}!")
                playerScore += 1
            else:
                print(f"\tRock smashes scissors! You lose round {i+1}.")
                IAScore += 1

if playerScore > IAScore: winner = 'PLAYER!!!'
elif playerScore < IAScore: winner = 'Computer :-('
else: winner = "Nobody wins, it's a tie!"
print(f'\nFinal Game Results\n\tRounds Played: {rounds}\n\tPlayer Score: {playerScore}\n\tComputer Score: {IAScore}\n\tWinner: {winner}')