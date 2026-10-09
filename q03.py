#) Leia 10 números inteiros em uma lista. Conte e envie quantos deles são pares .
#Exemplo: 3 8 5 12 7 4 9 10 1 6 → Quantidade de pares: 5.
 
numeros = []   

for i in range(10):
    numero = int(input("Digite um número:"))
    numeros.append(numero)
print("Números:", numeros)

for j in range(10):

    if numero % 2 == 0:
        numero += 1
print("Quantidade de pares:", numero)