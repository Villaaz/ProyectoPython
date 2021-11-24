print('Welcome to the Letter Counter App')

name = input('What is your name? ').title()

print(f'\nHello {name}!\nI will count the number of times that a specific letter occurs in a message.')

message = input('\nPlease enter a message: ')

letter = input('\nWhich letter would you like to count the occurences of? ').lower()
letter_count = message.count(letter)

print(f"\n{name}, your message has {letter_count} {letter}'s in it.")