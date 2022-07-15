# Faça um algoritmo que leia a preço de um produto e mostre seu novo preço, com 5% de desconto.

product = int(input('Enter the price R$ '))
discount = product - (product * 5 / 100)
print(f'Total with discount is R${discount}')