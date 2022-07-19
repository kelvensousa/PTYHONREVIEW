# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

name = str(input('Enter your name: ')).lower().title().strip()

print('Silva' in name)