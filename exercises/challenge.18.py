#18) Um professor quer sortear alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e
# escrevendo o nome do escolhido.
from random import choice
student0 = input("Enter the student's first name: ")
student1 = input("Enter the student's second name: ")
student2 = input("Enter the student's third name: ")
student3 = input("Enter the student's fourth name: ")
label = [student0, student1, student2, student3]
student = choice(label)
print(f'The randomly selected student who will erase the board is {student}! Gratters')

