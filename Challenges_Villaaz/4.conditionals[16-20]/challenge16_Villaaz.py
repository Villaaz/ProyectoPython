users = ['eramom', 'footea', 'davisv', 'papinukt', 'allenj']

print('\nWelcome to the Shipping Accounts Program')
user = input('\nHello, what is your username: ').lower()
if user in users:
    print(f'\nHello {user}. Welcome back to your account.\nCurrent shipping prices are as follows:')
    print('\nShipping orders 0 to 100:\t$5.10 each\nShipping orders 100 to 500:\t$5.00 each')
    print('Shipping orders 500 to 1000:\t$4.95 each\nShipping orders over 1000:\t$4.80 each')
    items = int(input('\nHow many items would you like to ship: '))
    if items > 0 and items <= 100:
        price = 5.10
    elif items > 100 and items <= 500:
        price = 5.0
    elif items > 500 and items <= 1000: 
        price = 4.95
    elif items > 1000:
        price = 4.80
    else:
        print('Please input a valid number.')
    totalPrice = round(items * price, 2)
    print(f'To ship {items} items it will cost you ${totalPrice} at ${price} per item.')
    place = input('\nWould you like to place this order (y/n): ').lower()
    if place == 'y':
        print(f'Okay. Shipping your {items} items.')
    elif place == 'n':
        print('Okay. No order is being placed at this time.')
else:
    print('Sorry, you do not have an account with us. Goodbye.')