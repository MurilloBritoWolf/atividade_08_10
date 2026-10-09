'''6) Leia uma lista de 10 inteiros e atribua o valor 0 a todos os elementos que forem negativos. Imprima a lista antes e depois da alteração.

Exemplo: [5 -3 8 -1 0 7 -9 2 4 -6] → [5 0 8 0 0 7 0 2 4 0].'''

lista = []

# injeção de elementos da lista
for i in range(10):
    numero = int(input('Digite um número inteiro: '))
    lista.append(numero)

print(lista)

# avaliação dos elementos na lista
for ii in range(10):
    if lista[ii] < 0:
        lista[ii] = 0

print(lista)
