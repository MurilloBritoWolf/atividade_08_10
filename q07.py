'''7) Leia uma lista de 10 números e um inteiro x. Conte e mostre todos os múltiplos de x presentes na lista.

Exemplo: lista [3 6 10 12 15 7 9 20 18 5], x = 3 → múltiplos: 3 6 12 15 9 18; quantidade: 6.'''

# injeção da lista e do inteiro x
lista = []

for i in range(10):
    numero = int(input(f'digite o {i + 1}° número: '))
    lista.append(numero)

x = int(input('digite o valor de relação com a lista: '))

# avaliação dos números multiplos por x
multiplos = []
for i in lista:
    if i % x == 0:
        multiplos.append(i)

# imressão do código
print(f'os multiplos de {x} na lista são: ', multiplos)
