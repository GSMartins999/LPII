# O seu programa deverá ler um arquivo texto onde cada linha possui uma string contendo
#  uma sequência de bases nitrogenadas de uma fita de DNA.
# Calcule quantas vezes cada base aparece em cada string lida e imprima os valores.

texto = str(input("Digite o texto : ")) .upper()
print("Analisando...")
print("A base nitrogenada Citosina apareceu {} vezes no texto." . format(texto.count('CITOSINA')))
print("A base nitrogenada Timina apareceu {} vezes no texto. " . format(texto.count('TIMINA')))
print("A base ntrogenada Guanina apareceu {} vezes no texto. " .format(texto.count('GUANINA')))
print("A base nitrogenada Adenina apareceu {} vezes no texto " .format(texto.count('ADENINA')))


