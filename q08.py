'''8) Leia dois vetores reais de 5 elementos cada. Imprima os dois vetores e calcule o produto escalar entre eles: x1*y1 + x2*y2 + ... + xn*yn.

Exemplo: [1, 2, 3, 4, 5] e [5, 4, 3, 2, 1] → produto escalar 35.'''

# injeção dos dois vetores
vetorX = []
vetorY = []

for j in range (5):
    numero = int(input(f'digite o {j + 1} número de X: '))
    vetorX.append(numero)

for j in range (5):
    numero = int(input(f'digite o {j + 1} número de Y: '))
    vetorY.append(numero)

# realizar o produto escalar
soma = 0
for j in range(5):
    soma += vetorX[j] * vetorY[j]

print(f' o produto escalar da lista {vetorX} e {vetorY} é {soma}')