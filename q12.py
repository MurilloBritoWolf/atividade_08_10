'''Leia uma matriz 3 × 3 de inteiros e calcule a soma dos elementos da diagonal principal (onde i == j).

Exemplo:

1 2 3
4 5 6
7 8 9

Soma da diagonal principal: 1 + 5 + 9 = 15.'''

# injeção dos dados na matriz
matriz = []

for i in range(3):
    numeros = []

    for j in range(3):
        numero = int (input('digite um número: '))
        numeros.append(numero)

    matriz.append(numeros)

# soma da diagonal + lista com os valores da diagonal
soma_diagonal = 0
lista_diagonal = []

for i in range(3):
    lista_diagonal.append(matriz[i][i])
    soma_diagonal += matriz[i][i]

# impressão da soma
print(f'a soma de {lista_diagonal} dá {soma_diagonal}')
