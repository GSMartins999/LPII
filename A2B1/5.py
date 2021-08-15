n = int(input('Digite um número: '))
vetor = []
a = 1
while a != n:
    cont = 0
for j in range(1, a+1):
    if (a % j == 0)and(a!=2):
        cont = cont + 1

if cont==2:
    vetor.append(a)
    a = a + 1
    print('Os números primos entre 1 e ',n,'são:',vetor)
