# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
name = input('What is your name? ')
money = float(input('How much money do you have? '))
print(f'{name}! You have R${money} real, and  you can buy ${(money / 5.24):.2f} dollars today.')