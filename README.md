# Atividade de Python: Vetores e Matrizes

> Curso de programação inicial em Python  
> Tema: listas (vetores) e listas de listas (matrizes)

| Questões | Valor total |
|:---:|:---:|
| 15 | 100 pontos |

## Sumário

- [Orientações](#orientações)
- [Nível 1: Vetores básicos](#nível-1-vetores-básicos)
- [Nível 2: Vetores intermediários e primeiras matrizes](#nível-2-vetores-intermediários-e-primeiras-matrizes)
- [Nível 3: Matrizes e algoritmos clássicos](#nível-3-matrizes-e-algoritmos-clássicos)
- [Critérios de avaliação](#critérios-de-avaliação)
- [Origem das questões](#origem-das-questões)

## Orientações

- Resolva cada questão em um arquivo separado, nomeado `q01.py`, `q02.py` e assim por diante.
- Use apenas recursos básicos: `input()`, `print()`, `if`, `for`, `while`, listas e índices.
- Evite atalhos prontos como `sum()`, `max()`, `min()` e `sort()` nas questões que pedem a lógica (somas, maior/menor e ordenação).
- Lembre que o primeiro índice de uma lista é **0**.
- Para criar uma matriz sem erro de cópia, use `[[0] * colunas for _ in range(linhas)]`.
- Teste cada programa com pelo menos dois conjuntos de valores.

---

## Nível 1: Vetores básicos

Valor: 6 pontos cada.

**1)** Crie uma lista `A` com 6 inteiros e execute, nesta ordem:

- a) atribua os valores `[1, 0, 5, -2, -5, 7]`;
- b) guarde em uma variável simples a soma de `A[0]`, `A[1]` e `A[5]` e mostre o resultado;
- c) modifique a posição 4, atribuindo o valor `100`;
- d) mostre cada elemento de `A`, um por linha.

*Resultado esperado:* a soma mostrada é `8`, e a lista final impressa é `1, 0, 5, -2, 100, 7`.

**2)** Leia 6 números inteiros, guarde-os em uma lista e mostre os valores lidos na **ordem inversa**.

*Exemplo:* entrada `1 2 3 4 5 6` → saída `6 5 4 3 2 1`.

**3)** Leia 10 números inteiros em uma lista. Conte e escreva quantos deles são **pares**.

*Exemplo:* `3 8 5 12 7 4 9 10 1 6` → `Quantidade de pares: 5`.

**4)** Leia 10 números inteiros em uma lista. Imprima a lista, o **maior elemento** e a **posição** (índice) em que ele se encontra.

*Exemplo:* lista `4 9 2 7 1 3 8 5 6 0` → `Maior: 9, posição: 1`.

**5)** Preencha uma lista com 10 números reais. Calcule e mostre a **quantidade de números negativos** e a **soma dos números positivos**.

*Exemplo:* `-2 3.5 4 -1 0 2 -7 1.5 6 -3` → `Negativos: 4` e `Soma dos positivos: 17.0`.

---

## Nível 2: Vetores intermediários e primeiras matrizes

Valor: 7 pontos cada.

**6)** Leia uma lista de 10 inteiros e atribua o valor `0` a todos os elementos que forem **negativos**. Imprima a lista antes e depois da alteração.

*Exemplo:* `5 -3 8 -1 0 7 -9 2 4 -6` → `5 0 8 0 0 7 0 2 4 0`.

**7)** Leia uma lista de 10 números e um inteiro `x`. Conte e mostre todos os **múltiplos de `x`** presentes na lista.

*Exemplo:* lista `3 6 10 12 15 7 9 20 18 5`, `x = 3` → múltiplos: `3 6 12 15 9 18`; quantidade: `6`.

**8)** Leia dois vetores reais de 5 elementos cada. Imprima os dois vetores e calcule o **produto escalar** entre eles: `x1*y1 + x2*y2 + ... + xn*yn`.

*Exemplo:* `[1, 2, 3, 4, 5]` e `[5, 4, 3, 2, 1]` → produto escalar `35`.

**9)** Leia uma matriz 4 × 4 de números inteiros. Conte e escreva quantos valores são **maiores que 10**.

*Dica:* use dois laços `for` aninhados, um para as linhas e outro para as colunas.

**10)** Crie uma matriz 5 × 5 preenchida com `1` na **diagonal principal** e `0` nos demais elementos. Ao final, imprima a matriz em linhas e colunas.

*Resultado esperado:*

```text
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
```

---

## Nível 3: Matrizes e algoritmos clássicos

Valor: 7 pontos cada.

**11)** Leia uma matriz 4 × 4 de inteiros, imprima a matriz e informe a **localização (linha e coluna) do maior valor**.

*Exemplo:* se o maior valor, `42`, está na terceira linha e segunda coluna, a saída deve indicar `linha 2, coluna 1` (contando a partir de 0) ou `linha 3, coluna 2` (contando a partir de 1). Escolha uma forma e indique no programa qual usou.

**12)** Leia uma matriz 3 × 3 de inteiros e calcule a **soma dos elementos da diagonal principal** (onde `i == j`).

*Exemplo:*

```text
1 2 3
4 5 6
7 8 9
```

Soma da diagonal principal: `1 + 5 + 9 = 15`.

**13)** Leia uma matriz 3 × 3 de inteiros e gere uma **lista com a soma de cada coluna**. Mostre a lista.

*Exemplo:*

```text
 5 -8 10
 1  2 15
25 10  7
```

Saída: `[31, 4, 32]`.

**14)** Leia 10 números inteiros em uma lista e escreva quais elementos são **números primos**, acompanhados de suas posições na lista.

*Lembrete:* um número primo é maior que 1 e divisível apenas por 1 e por ele mesmo.

*Exemplo:* lista `4 7 10 13 1 9 2 15 17 20` → primos: `7 (posição 1)`, `13 (posição 3)`, `2 (posição 6)`, `17 (posição 8)`.

**15)** Leia uma lista de 10 números reais, **ordene os elementos em ordem crescente** usando um algoritmo implementado por você (por exemplo, Bubble Sort ou Selection Sort) e escreva a lista ordenada.

*Exemplo:* `5 2 9 1 7 3 8 6 4 0` → `0 1 2 3 4 5 6 7 8 9`.

---

## Critérios de avaliação

| Critério | Peso |
|---|:---:|
| O programa executa sem erros e produz a saída correta | 60% |
| Uso adequado de listas, índices e laços | 20% |
| Lógica própria, sem atalhos prontos quando não permitidos | 10% |
| Organização do código, nomes claros de variáveis e comentários | 10% |

## Origem das questões

| Questão | Origem no caderno |
|:---:|---|
| 1 | Vetores 01 |
| 2 | Vetores 08 |
| 3 | Vetores 05 |
| 4 | Vetores 07 |
| 5 | Vetores 11 |
| 6 | Vetores 17 |
| 7 | Vetores 18 |
| 8 | Vetores 23 |
| 9 | Matrizes 01 |
| 10 | Matrizes 02 |
| 11 | Matrizes 04 |
| 12 | Matrizes 10 |
| 13 | Matrizes 18 |
| 14 | Vetores 27 |
| 15 | Vetores 36 |
