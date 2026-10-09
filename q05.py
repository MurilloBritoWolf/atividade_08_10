# 5) Preencha uma lista com 10 números reais. Calcule e mostre a quantidade de números negativos e a soma dos números positivos.


numeros = [-2, 3, 4, -1, 0, 2, -7, 1.5, 6, -3]

quantidade_negativos = 0

soma_positivos = 0

for numero in numeros:

    if numero < 0:
        quantidade_negativos += 1
    elif numero > 0:
        soma_positivos += numero


print("Lista de Números:", numeros)
print("Quantidade de Números Negativos:", quantidade_negativos)
print("Soma dos Números Positivos:", soma_positivos)
