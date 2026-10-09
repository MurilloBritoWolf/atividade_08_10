#15) Leia uma lista de 10 números reais, ordene os elementos em 
# ordem crescente usando um algoritmo implementado por você (por exemplo, 
# Bubble Sort ou Selection Sort) e escreva a lista ordenada.

#Exemplo: 5 2 9 1 7 3 8 6 4 0 → 0 1 2 3 4 5 6 7 8 9.

numeros = []

for i in range(10):
    numero = float(input("Digite um número real aleatório:"))
    numeros.append(numero)

print(numeros)

for i in range(9):
    for j in range(9):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print(numeros)