#16) Faça um programa que leia o comprimento do cateto oposto e do cate adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input("Enter with the opposite side: "))
ca = float(input("Enter with the adjacent side: "))
hypo = hypot(co , ca)
print(f'The hypotenuse of a right triangle with the values of the opposite side equivalent to {co} and the side adjacent to {ca} is {hypo:.2f}. ')

