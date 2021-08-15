n = int(input('Informe um número: '))
a = n
b = 1

print('Calculando {}! = '.format(n), end='')
while a > 0:
    print('{}'.format(a), end='')
    print(' x ' if a > 1 else ' = ', end='')
    b *= a
    a -= 1
print('{}'.format(b)) 
