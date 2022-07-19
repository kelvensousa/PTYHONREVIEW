# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "Santo"

town = input('Town: ').strip().split()
print(f'Entered town name starts with "SANTO": ', 'SANTO' in {town[0].upper()})