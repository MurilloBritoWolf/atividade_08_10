#) Leia 10 números inteiros em uma lista. Conte e envie quantos deles são pares .
#Exemplo: 3 8 5 12 7 4 9 10 1 6 → Quantidade de pares: 5.
 
numeros = []   

for i in range(10):
    numero = int(input("Digite um número:"))
    numeros.append(numero)
print("Números:", numeros)
#Pede para o usuário digitar os números e depois imprime a lista.

quantidade = 0

for numero in numeros: 
        if numero % 2 == 0:
            quantidade += 1
print("Quantidade de pares:", quantidade) 
#verifica quantos números são pares na lista, faz a contagem dos números pares e imprime.                                        