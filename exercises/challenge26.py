# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# Ex: Ana Maria de Sousa
# primeiro = Ana
# ultimo = Sousa

name = input('Enter your name: ').strip().lower().title().split()

print(f'Your first name is: {name[0]}')
print(f'Your second name is: {name[len(name) -1]}')