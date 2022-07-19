# Faça um programa que leia um numero de 0 a 9999 e mostre na tela um dos digitos separados.
# Ex: Digite um numero: 1895
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1


number = str(input('Enter a number 0 between 9999: ')).zfill(4)

print('The enter number is: {}'.format(number))
print('Your unity is: {}'.format(number[3]))
print('Your ten is: {}'.format(number[2]))
print('Your hundred is: {}'.format(number[1]))
print('Your thousand is: {}'.format(number[0]))