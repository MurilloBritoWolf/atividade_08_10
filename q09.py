#9) Leia uma matriz 4 × 4 de números inteiros. Conte e escreva quantos valores são maiores que 10.
#Dica: use dois laços for aninhados, um para as linhas e outro para as colunas.

mat = [
    [3, 7, 12, 7],
    [15, 6, 74, 8],
    [14, 34, 8, 2],
    [1, 10, 5, 21,]
]

maior = []
con = 0 
 
for lin in mat:
    for num in lin:
        if num > 10:
            maior.append(num)

for i in maior:
    print(i) 
    con += 1

print("Quantos números são maior que 10:",con)