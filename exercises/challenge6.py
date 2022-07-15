# Desenvolva um programa que leia as duas três de um aluno, calcule e mostre a sua média.

student = input('Enter the name of student: ')
test = float(input('Enter the note: '))
homework = float(input('Enter the note: '))
task = float(input('Enter the note: '))
result = (test + homework + task) / 3
print(f'{student} your note of test is {test}, your homework is {homework}, and your  task is {task}, and your average is {(result):.1f}.')
