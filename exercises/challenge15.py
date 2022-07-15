# 15) Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um numero: 6.127 o numero 6.127 tem a parte inteira 6.
import math


num = float(input('Enter a number: '))
number = math.floor(num)
print(f'The {num} integer corresponds {number}.')
