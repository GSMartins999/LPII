#O seu programa deverá ler um arquivo texto onde 
# cada linha possui uma string contendo uma sequência de bases nitrogenadas de uma fita de DNA. 
#Encontre a fita suplementar de cada DNA e a imprima no console.


from os import replace

with open("ativi.txt", "r") as var:

 recebevar = var.readlines()

print (recebevar)

i = 0

while i < len(recebevar):

    x = recebevar[i]

    y1 = x.replace("G","c")

    y2 = y1.replace("C","g")

    y3 = y2.replace("A","t")

    y4 = y3.replace("T","a")

    print('\n') 

    print(("Linha"),(i+1),("original: "),(x))

    print(("Escreva a linha"),(i+1),(":"),(y4.upper()))
    
    i = i + 1

