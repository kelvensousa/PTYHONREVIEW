# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

employee = input('Enter employee name: ')
income = float(input('Enter the value of income: '))
new_increase = income + (income * 15/100)
print(f'{employee}! Your new income is R${(new_increase):.3f}')
