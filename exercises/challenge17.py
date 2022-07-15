#17) Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse angulo.

import math

angle = float(input("Enter with the number of angle: "))
sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))
print(f'The angles is {angle} and o cosine is {cosine:.2f}, the sine is {sine:.2f} and the tangent is {tangent:.2f}.')