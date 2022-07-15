# adding with numerators
i = 8 + 5
g = '8' + '6'
h = 'aba' + 'ca' + 'te'
p = 5*9
ç = 5//9
s = 8%9
j = 8-9
o = 8/2
a = 78**52
l = 'ave' + '52'
print(i, g, h, p, ç, s, j, o, a, l)
#-------------------------------------------------------------------------------------------------
print('='*20)
name = input('Whats your name? ')
print('Nice to meet you {:^20}!'.format(name))
print('=>'*22)
name = input('Whats your name? ')
print('Nice to meet you {:=^20}!'.format(name))
print('=>'*30)
name = input('Whats your name? ')
print('Nice to meet you {}!'.format(name))
print('='*60)

number = int(input('Enter a number: '))
numbers = int(input('Enter other a number: '))
s = number * numbers
d = number + numbers
e = number / numbers
f = number // numbers
g = number ** numbers
print('The sun is {}, \n the product is {} the \n division is {:.3f}'.format(s, d, e, f, g,), end=' ')
print('The division entire {} is potency {}'.format(e, f))

