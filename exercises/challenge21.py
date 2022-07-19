# Crie um programa que o nome completo e uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minuscules.
# Quantas letras tem ao todo (sem considerar os espaços).
# Quantas letras tem o primeiro nome.

name = input("What's your name? ").strip()
division = name.split()
n = name.upper() # uppercase the letters
a = name.lower() # lowercase the letters
m = len(name) # character count
e = len(division[0]) # first name with characters count
print(f'Your name in uppercase is: {n}')
print(f'Your name in lowercase is: {a}')
print(f'Your name with characters count is: {m}')
print(f'Your first name with characters count is: {e}')




