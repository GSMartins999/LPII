#O seu programa deverá ler um arquivo texto onde cada linha possui uma string contendo uma
#sequência de bases nitrogenadas de uma fita de DNA. Para cada linha lida faça a transcrição 
#para a fita de RNA equivalente.

from os import replace

with open("ativi.txt", "r") as var:

 recebevar = var.readlines()

print (recebevar)

i = 0

while i < len(recebevar):

    x = recebevar[i]

    v1 = x.replace("G","c")

    v2 = v1.replace("C","g")

    v3 = v2.replace("A","u")

    v4 = v3.replace("T","a")

    print('\n') 

    print(("Linha"),(i+1),("original: "),(x))

    print(("Escreva a linha"),(i+1),(":"),(v4.upper()))
    
    i = i + 1