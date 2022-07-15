# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2.

width = float(input('Enter the large: '))
height = float(input('Enter the height: '))
meters = width * height
ink = meters / 2
print(f'You will spend {(ink):.2f} liters of ink to paint {meters}m².')

