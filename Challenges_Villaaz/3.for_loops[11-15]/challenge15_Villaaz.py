print('\nWelcome to the Average Calculator App')
nombre = input('\nWhat is your name: ').title()
num = int(input('How many grades would you like to enter: '))
notas = []
for i in range(num):
    notas.append(int(input('Enter grade: ')))

notas = sorted(notas, reverse=True)
print('\nGrades Highest to Lowest:')
for i in range(num):
    print('\t', notas[i])

suma = sum(notas)
avg = round(float(suma/num), 2)
print(f"\n{nombre}'s Grade Summary:")
print(f'\tTotal Number of Grades: {num}')
print(f'\tHighest Grade: {notas[0]}')
print(f'\tLowest Grade: {notas[num-1]}')
print(f'\tAverage: {avg}')

desAvg = float(input('\nWhat is your desired average: '))
notaExtra = (desAvg * (num+1)) - suma
print(f'\nGood luck {nombre}!')
print(f'You will need to get a {notaExtra} on your next assignment to earn a {desAvg} average.')
notasCopia = notas
print(f"\nLet's see what your average could have been if you did better/worse on an assignment.")
notaBusca = int(input('What grade would you like to change: '))
notaCambio = int(input(f'What grade would you like to change {notaBusca} to: '))
if notaBusca in notasCopia:
    notasCopia.remove(notaBusca)
    notasCopia.append(notaCambio)
else:
    print(f'{notaBusca} no está en tu lista de notas')

notasCopia = sorted(notasCopia, reverse=True)
print('\nNew Grades Highest to Lowest:')
for i in range(num):
    print('\t', notasCopia[i])

sumaCopia = sum(notasCopia)
avgCopia = round(float(sumaCopia/num), 2)
print(f"\n{nombre}'s New Grade Summary:")
print(f'\tTotal Number of Grades: {num}')
print(f'\tHighest Grade: {notasCopia[0]}')
print(f'\tLowest Grade: {notasCopia[num-1]}')
print(f'\tAverage: {avgCopia}')

print(f'\nYour new average would be a {avgCopia} compared to you real average of {avg}!')
change = round(avgCopia-avg, 2)
print(f'That is a change of {change} points!')
print(f'\nToo bad your original grades are still the same!\n{notas}\nYou should go ask for extra credit!')
# Por qué notas sale como notasCopia no entiendo???????????????' no lo cambio en ningún momento