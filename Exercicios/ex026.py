"""
Exercício Python 26: 
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""

frase = str(input("Digite uma frase: "))

print("A letra A aparece {} vezes na frase.".format(frase.lower().count('a')))
print("A primeira letra A apareceu na posição {}".format(frase.strip().find("a")+1))
print("A última letra A apareceu na posição {}".format(frase.strip().rfind("a")+1))