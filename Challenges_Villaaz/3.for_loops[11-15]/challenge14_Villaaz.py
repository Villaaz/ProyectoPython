print('\nWelcome to the Fibonacci Calculator App')
tope = int(input('How many digits of the Fibonacci Sequence would you like to compute: '))
num1 = 0
num2 = 1
sum = 0
ratio = []
print(f'The first {tope} numbers of the Fibonacci sequence are:')
for i in range(0, tope):  
    num1 = num2
    num2 = sum
    sum = num1 + num2
    print(sum)
    ratio.append((num2/sum)+1)

print('\nThe corresponding Golden Ratio values are:')
for i in ratio:
    print(i)