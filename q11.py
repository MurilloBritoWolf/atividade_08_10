'''11) Leia uma matriz 4 × 4 de inteiros, imprima a matriz e informe a localização (linha e coluna) do maior valor.

Exemplo: se o maior valor, 42, está na terceira linha e segunda coluna, a saída deve indicar linha 2, coluna 1 
(contando a partir de 0) ou linha 3, coluna 2 (contando a partir de 1). Escolha uma forma e indique no programa qual usou.'''


# injeção da matriz escolhida
matriz = []

for i in range(4):
    lista = []

    for j in range (4):
        numero = int(input('digite um número: '))
        lista.append(numero)

    matriz.append(lista)


# seleção do maior
maior = matriz [0][0]

for i in matriz:
    for j in i:
        if j > maior:
            maior = j

# localizar o maior
for i in range(4):
    for j in range(4):
        if matriz[i][j] == maior:
            print(f'número maior {maior} na fileira: {i}; coluna: {j}')

