import math

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
print('Welcome to the Right Triangle Solver App')

first_leg = input('\nWhat is the first leg of the triangle: ')
if is_number(first_leg) == False:
  print('\nPlease enter a valid number.')
else:
  second_leg = input('What is the second leg of the triangle: ')
  if is_number(second_leg) == False:
    print('\nPlease enter a valid number.')
  else:

    # El teorema de Pitágoras es h = √ a² + b²
    hypotenuse = (float(first_leg) ** 2) + (float(second_leg) ** 2)
    area = round((float(first_leg) * float(second_leg)) / 2, 3)
    hypotenuse = round(math.sqrt(hypotenuse), 3)

    print(f'\nFor a triangle with legs of {first_leg} and {second_leg} the hypotenuse is {hypotenuse}.')
    print(f'For a triangle with legs of {first_leg} and {second_leg} the area is {area}.')