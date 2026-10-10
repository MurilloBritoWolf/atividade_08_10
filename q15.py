#15) Leia uma lista de 10 números reais, ordene os elementos em 
# ordem crescente usando um algoritmo implementado por você (por exemplo, 
# Bubble Sort ou Selection Sort) e escreva a lista ordenada.

#Exemplo: 5 2 9 1 7 3 8 6 4 0 → 0 1 2 3 4 5 6 7 8 9.

numeros = [] #criando uma lista vazia

for i in range(10):  #usando for para percorrer a lista por 10 vezes
    numero = float(input("Digite um número real aleatório:")) #criando a variável número p/ receber o número digitado pelo usuário
    numeros.append(numero) #adicionando cada número na lista vazia

print(numeros) #mostrando a lista preenchida para o usuario

for i in range(9): #percorrer a lista
    for j in range(9):  #percorrer cada item da lista
        if numeros[j] > numeros[j + 1]: #usando condicional p/ comparar cada número com seu vizinho a direita, vendo se é maior
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j] #caso seja, o numero maior é jogado p/ direita, ordenando os numeros de maneira crescente 

print(numeros) #mostrando a lista em ordem crescente para o usuario
