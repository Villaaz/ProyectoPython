import datetime

time = datetime.datetime.now()
month = int(time.month)
day = int(time.day)
hour = int(time.hour) + 2
minute = int(time.minute)

# Intro
print('Welcome to the Grocery List App.')
print(f'Current Date and Time: {month}/{day} {hour}:{minute}')
print('You currently have Meat and Cheese in your list.')

# línea 25
groceries = ["Meat", "Cheese"]

# inputs de los nuevos items
item = input('\nType of food to add to the grocery list: ').strip().title()
groceries.append(item)
item = input('Type of food to add to the grocery list: ').strip().title()
groceries.append(item)
item = input('Type of food to add to the grocery list: ').strip().title()
groceries.append(item)

# sorting solo funciona en strings si los items están con dobles comillas (""), NO FUNCIONA con comillas simples ('')
print(f'\nHere is your grocery list:\n{groceries}')
groceries = sorted(groceries)
print(f'Here is your grocery list sorted:\n{groceries}')

print('\nSimulating grocery shopping...')

# compra nº1
print(f'\nCurrent grocery list: {len(groceries)} items')
print(groceries)
purchase = input('What food did you just buy: ').strip().title()
print(f'Removing {purchase} from list...')
groceries.remove(purchase)

# compra nº2
print(f'\nCurrent grocery list: {len(groceries)} items')
print(groceries)
purchase = input('What food did you just buy: ').strip().title()
print(f'Removing {purchase} from list...')
groceries.remove(purchase)

# compra nº3
print(f'\nCurrent grocery list: {len(groceries)} items')
print(groceries)
purchase = input('What food did you just buy: ').strip().title()
print(f'Removing {purchase} from list...')
groceries.remove(purchase)

print(f'\nCurrent grocery list: {len(groceries)} items')
print(f'\n{groceries}')

# item agotado
print(f'\nSorry, the store is out of {groceries[1]}.')
groceries.remove(groceries[1])
item = input('What food would you like instead: ').strip().title()
groceries.insert(0, item)

print(f'\nHere is what remains on your grocery list:\n{groceries}')