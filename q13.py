13) Leia uma matriz 3 × 3 de inteiros e gere uma lista com a soma de cada coluna. Mostre a lista.

matriz = [
    [1, 3, 4],
    [9, 8, 5],
    [2, 6, 7]
]

somas = []

for coluna in range(3):

    soma = 0

    for linha in range(3):
        soma += matriz[linha][coluna]
    somas.append(soma)

print("A soma de cada coluna em sequência é:", somas)

