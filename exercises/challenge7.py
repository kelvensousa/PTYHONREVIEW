# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

'''value = float(input('Enter the value: '))
cm = value * 100
mm = value * 1000
print(f'{value} meters is equal {cm} centimeters and {mm} millimeters.')'''
value = float(input('Enter the value: '))
print(f'{value} meters is equal {(value * 100):.2f} centimeters and {(value * 1000):.2f} millimeters.')