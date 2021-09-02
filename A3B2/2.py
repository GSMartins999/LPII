N, M = [int(value) for value in input('\n Informe o total de amigos do grupo e quantas reuniões aconteceram: ').split()]

print('\n Pessoas Infectadas e Reuniões')
I, R = [int(value) for value in input('\n Informe o número de infectados e a reunião em que participaram infectados: ').split()]
restricoes = False

restricoes = True if 2<N and N<1000 else restricoes
restricoes = True if 2<M and M<1000 else restricoes
restricoes = True if 1<I and I<N else restricoes
restricoes = True if 1<R and R<M else restricoes

reunioes = []
infectados = {I}

print('\n informações das reuniões')
print('*Participantes da reunião 1, Participantes da reunião 2 e assim por diante... \n')

for value in range(M):
    reunioes.append([int(value) for value in input('-> ').split()])
    restricoes = True if 1<reunioes[-1][0] and reunioes[-1][0]<N else restricoes
    reunioes[-1].pop(0)
    restricoes = True if any(P<1 and N<P for P in reunioes[-1]) else restricoes

if restricoes:
    for i in range (R-1, M):
        if any(pessoa in infectados for pessoa in reunioes[i]):
            infectados.update(reunioes[i])

print('\n O total de pessoas infectadas é : ')
print(len(infectados))