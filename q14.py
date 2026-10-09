lista = [4, 7, 10, 13, 1, 9, 2, 15, 17, 20]

for i in lista:             #Percorre a lista
    if i < 2:               #Se menor que não já não é primo
        print(f'O numero {i} não é Primo 1!')

    else:
        primo = True        # Define primo como Bol Verdadeiro

        for x in range(2, i):   # Percorre entre 2 e o numero testado
            if i % x == 0:      # Verifica se o num testado divide por algum num entre 2 e ele mesmo
                primo = False   # Muda a Variavel para Bol Falso se Confirmar o IF da lin 11
                break

        if primo:               #Verifica se a variavel primo é verdadeira/True ou Falsa/False
            print(f'O numero {i} é Primo 2!')

        else:
            print(f'O numero {i} não é Primo 3!')