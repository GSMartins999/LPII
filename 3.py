def s(a,b):
    soma = a + b
    if soma > 1000:
        raise OverflowError
    else:
        print(soma)

try:
    x = int(input('Digite um número: '))
    y = int(input('Digite um número: '))
    s(x,y)

except OverflowError:
    print('O resultado da soma é um valor acima de mil! \nPor isso não é possível exibi-lo.')