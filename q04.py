# 4) Leia 10 números inteiros em uma lista. Imprima a lista, o maior elemento e a posição (índice) em que ele se encontra.

numeros = [4, 6, 8, 1, 0, 2, 3, 5, 7, 9,]

for numero in numeros:

    maior = numeros[0]
    
    if numero > maior:
       maior = numero
posicao = numeros.index(maior)

print("Lista:", numeros)
print("Maior Número:", maior)
print("Posição do Maior Número:", posicao)
