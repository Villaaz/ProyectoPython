def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
print('Welcome to the Multiplication/Exponent Table App')

name = input('\nWhat is your name? ').title()
num = float(input('What number would you like to work with? '))
if is_number(num) == False:
  print('Please enter a valid number')

print('\nMultiplication Table For', num)

print(f'\n\t1.0 * {num} = {round(1*num,4)}\n\t2.0 * {num} = {round(2*num,4)}\n\t3.0 * {num} = {round(3*num,4)}\n\t4.0 * {num} = {round(4*num,4)}\n\t5.0 * {num} = {round(5*num,4)}\n\t6.0 * {num} = {round(6*num,4)}\n\t7.0 * {num} = {round(7*num,4)}\n\t8.0 * {num} = {round(8*num,4)}\n\t9.0 * {num} = {round(9*num,4)}')

print(f'\nExponent Table For {num}')

print(f'\n\t{num} ** 1 = {round(num**1,4)}\n\t{num} ** 2 = {round(num**2,4)}\n\t{num} ** 3 = {round(num**3,4)}\n\t{num} ** 4 = {round(num**4,4)}\n\t{num} ** 5 = {round(num**5,4)}\n\t{num} ** 6 = {round(num**6,4)}\n\t{num} ** 7 = {round(num**7,4)}\n\t{num} ** 8 = {round(num**8,4)}\n\t{num} ** 9 = {round(num**9,4)}\n')

message = name + ' Math is cool!'
print(message, '\n\t', message.lower(), '\n\t\t', message.title(), '\n\t\t\t', message.upper())