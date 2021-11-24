import math

print('\nWelcome to the Factorial Calculator App')
num = int(input('\nWhat number would you like to compute the factorial of? '))
print(f'{num}! =', end= " ")

for i in range(1, num+1):
    if i == num:
        print(i, end=" ")
        break
    else:
        print(i, end="*")

suma = 1
for i in range(1, num+1):
    suma *= i

print(f'\nHere is the result form the math library:\nThe factorial of {num} is {math.factorial(num)}!')
print(f'\nHere is the result from my own algorithm:\nThe factorial of 10 is {suma}!')
print(f'\nIt is shown twice that {num}! = {suma} (with excitement)')