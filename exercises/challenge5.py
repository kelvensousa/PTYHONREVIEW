# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

import math
number = float(input('Enter a number: '))
print(f'The number is {number} and your double is {number * 2}, you triple is {number * 3}.')
print('Your square root is', pow(number,(1/2)))
'''###import math  this is the second code
number = float(input('Enter a number: '))
num = number * 2
num1 = number * 3
print(f'The number is {number} and your double is {num}, you triple is {num1}.')
print('Your square root is', math.sqrt(number))'''