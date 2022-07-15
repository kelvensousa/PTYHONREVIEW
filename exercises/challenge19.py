#19) O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um
# Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.

from random import shuffle
student0 = input("Enter the student's first name: ")
student1 = input("Enter the student's secund name: ")
student2 = input("Enter the student's third name: ")
student3 = input("Enter the student's fouth name: ")
label = [student0, student1, student2, student3]
shuffle(label)
print(f'The order of students drawn is {label}! Gratters.')