print('\nWelcome to the Binary/Hexadecimal Converter App')
num = int(input('\nCompute binary and hexadecimal values up to the following decimal number: '))
decimal = list(range(1, num+1))
binary = []
hexadecimal = []
for i in decimal:
    binary.append(bin(i))
    hexadecimal.append(hex(i))
print('Generating lists....complete!')
print('\nUsing slices, we will now show a portion of each list.')
start = int(input('What decimal number would you like to start at: '))
end = int(input('What decimal number would you like to stop at: '))

print(f'\nDecimal values from {start} to {end}:')
for i in range(start-1, end):
    print(decimal[i])

print(f'\nBinary values from {start} to {end}:')
for i in range(start-1, end):
    print(binary[i])

print(f'\nHexadecimal values from {start} to {end}:')
for i in range(start-1, end):
    print(hexadecimal[i])

input(f'\nPress Enter to see all values from 1 to {num}.')
print('Decimal----Binary----Hexadecimal\n----------------------------------------------------------')
for i in range(0, num):
    print(f'{decimal[i]}----{binary[i]}----{hexadecimal[i]}')