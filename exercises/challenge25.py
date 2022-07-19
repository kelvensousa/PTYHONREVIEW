# Faça um programa qu leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez.

pharse = input('Digite uma frase: ').strip().lower()

# print(Quantidade de vezes que a letra "A" aparece: frase.count("A")
print(f'How many time the letter "a" showing? {pharse.count("a")}')

# print(Em que posição o A aparece a primeira vez: frase.find("A")
print(f'In what position the letter "a" showing first turn? {pharse.find("a") + 1}')

# print(Em que posição o "A" aparece pela ultima vez: frase.rfind("A")
print(f'In what position the letter "a" showing last turn? {pharse.rfind("a") + 1}')
