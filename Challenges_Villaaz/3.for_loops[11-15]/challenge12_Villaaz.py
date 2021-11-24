import cmath

print('\nWelcome to the Quadratic Equation Solver App.')
print('\nA quadratic equation is of the form ax^2 + bx + c = 0')
print('Your solutions can be real or complex numbers.')
print('A complex number has two parts: a + bj ')
print('Where a is the real portion and bj is the imaginary portion.')
n = int(input('How many equations would you like to solve today: '))
for i in range(n):
    print(f'\nSolving equation #{i+1}\n---------------------------------------------------------------')
    a = float(input('\nPlease enter your value of a (coefficient of x^2): '))
    b = float(input('Please enter your value of b (coefficient of x): '))
    c = float(input('Please enter your value of c (coefficient): '))

    discriminante =  b * b - 4 * a * c

    if discriminante < 0: 
        print(f'\nLa ecuación no tiene soluciones reales.')
    else:
        raiz = cmath.sqrt(discriminante)
        x_1 = (-b + raiz) / (2 * a)
        if discriminante != 0:
            x_2 = (-b - raiz) / (2 * a)
            print(f'\nLas soluciones son {x_1} y {x_2}.')
        else:
            print(f'\nLa única solución es x = {x_1}')