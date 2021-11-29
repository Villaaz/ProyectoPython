parties = ['Republican', 'Democratic', 'Independent', 'Libertarian', 'Green']
print('\nWelcome to the Voter Registration App')
name = input('\nPlease enter your name: ').title()
age = int(input('Please enter your age: '))
if age < 18:
    print('\nYou are not old enough to vote.')
else:
    print(f'\nCongratulations {name}! You are old enough to register to vote.')
    print(f'\nHere is a list of political parties to join.\n\t-{parties[0]}\n\t-{parties[1]}\n\t-{parties[2]}\n\t-{parties[3]}\n\t-{parties[4]}')
    join = input('\nWhat party would you like to join: ').title()
    print(f'\nCongratulations {name}! You have joined the {join} party!')
    if join == parties[0]:
        print('That is a major party!')
    elif join == parties[1]:
        print('This is a major party!')
    elif join == parties[2]:
        print('You are an independent person!')
    else:
        print('That is not a major party!')