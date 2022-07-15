#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a
#quantidade de dias pelos quais foi alugado. Calcule o preço a pagar, sabendo que o carro
#custa R$60 por dia e R$0.15 por km rodado.

client = input("What's your name? ")
km = flaot(input("Enter with the number KM? "))
days = int(input("How much days do want to rent? "))
print(f'Hello {client}, you will run {km} KM and rented for {days} days.')
print(f'{client} you will pay R$ {(60 * days) + (km * 0.15) +400} (included R$300 rent taxes + R$100 insurance taxes). ')
