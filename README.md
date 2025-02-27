# Algoritmo de Karatsuba

O *Algoritmo de Karatsuba* é um método eficiente para multiplicação de números inteiros grandes, desenvolvido por Anatolii Karatsuba em 1960. Este projeto implementa o algoritmo em Python, demonstrando como ele consegue melhorar a complexidade da multiplicação em comparação ao método tradicional.

## Multiplicação de Números Grandes

A multiplicação de números grandes é um problema fundamental na computação. O método tradicional de multiplicação tem complexidade O(n²), onde n é o número de dígitos. O algoritmo de Karatsuba oferece uma melhoria significativa, reduzindo a complexidade para O(n^log₂3) ≈ O(n^1.585).

## Técnica "Dividir para Conquistar"

O algoritmo de Karatsuba utiliza a técnica de "dividir para conquistar", que consiste em:

1. Dividir o problema em subproblemas menores
2. Resolver os subproblemas recursivamente
3. Combinar as soluções dos subproblemas

Para dois números x e y de n dígitos, o algoritmo:
1. Divide cada número em duas partes
2. Realiza três multiplicações menores em vez de quatro
3. Combina os resultados usando adições e subtrações

## Análise de Complexidade

### Complexidade Assintótica

#### Complexidade Temporal
- *Melhor Caso*: O(1)
  - Ocorre quando um dos números tem apenas um dígito
  - Neste caso, o algoritmo retorna imediatamente o produto direto

- *Caso Médio e Pior Caso*: O(n^log₂3) ≈ O(n^1.585)
  - Onde n é o número de dígitos do maior número
  - A cada chamada recursiva, o tamanho do problema é reduzido pela metade
  - São feitas 3 chamadas recursivas para números de tamanho n/2
  - Pelo Teorema Mestre, isso resulta em complexidade O(n^log₂3)

#### Complexidade Espacial
- *O(n)* devido à pilha de recursão
  - Cada chamada recursiva armazena um conjunto constante de variáveis
  - A profundidade da recursão é O(log n)
  - O espaço total necessário é proporcional à profundidade da recursão

### Complexidade Ciclomática

#### Estrutura do Grafo de Fluxo
1. *Nós (N):* 8
   - Entrada da função
   - Verificação do caso base
   - Cálculo do número de dígitos
   - Divisão dos números
   - Cálculo do produto das partes altas
   - Cálculo do produto das partes baixas
   - Cálculo do termo do meio
   - Retorno do resultado

2. *Arestas (E):* 9
   - Entrada → Verificação do caso base
   - Verificação → Retorno (caso base verdadeiro)
   - Verificação → Cálculo de dígitos (caso base falso)
   - Cálculo de dígitos → Divisão
   - Divisão → Produto das partes altas
   - Produto das partes altas → Produto das partes baixas
   - Produto das partes baixas → Termo do meio
   - Termo do meio → Combinação final
   - Combinação final → Retorno

3. *Componentes Conexos (P):* 1
   - O grafo forma um único componente conexo

#### Cálculo da Complexidade Ciclomática
- *Fórmula:* M = E - N + 2P
- *Cálculo:* M = 9 - 8 + 2(1) = 3
- *Interpretação:* 
  - O valor 3 indica baixa complexidade
  - Existem 3 caminhos independentes no código
  - Facilita a manutenção e os testes

### Comparação com Multiplicação Tradicional

| Aspecto | Multiplicação Tradicional | Algoritmo de Karatsuba |
|---------|-------------------------|----------------------|
| Complexidade Temporal | O(n²) | O(n^1.585) |
| Complexidade Espacial | O(1) | O(n) |
| Simplicidade do Código | Alta | Média |
| Eficiência para Números Grandes | Menor | Maior |

## Ambiente de Desenvolvimento

### Requisitos
- Python 3.x

### Como executar

1. Clone este repositório:
bash
git clone [URL_DO_REPOSITÓRIO]


2. Execute o script principal:
bash
python main.py


## Explicação do Código

### Arquivo: main.py

#### karatsuba(x, y)
- *Objetivo:* Multiplica dois números inteiros usando o algoritmo de Karatsuba
- *Parâmetros:*
  - x: Primeiro número inteiro
  - y: Segundo número inteiro
- *Retorno:*
  - Produto de x e y

#### Estrutura do algoritmo:

1. *Caso Base:*
python
if x < 10 or y < 10:
    return x * y

- Quando os números são pequenos, usa multiplicação direta

2. *Divisão:*
python
n = max(len(str(x)), len(str(y)))
m = n // 2
divisor = 10 ** m
a = x // divisor
b = x % divisor
c = y // divisor
d = y % divisor

- Divide os números em partes alta (a,c) e baixa (b,d)

3. *Conquista:*
python
ac = karatsuba(a, c)
bd = karatsuba(b, d)
ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

- Calcula os produtos necessários recursivamente

4. *Combinação:*
python
return ac * 10**(2*m) + ad_plus_bc * 10**m + bd

- Combina os resultados para obter o produto final

## Resultados dos Testes

O algoritmo foi testado com diversos casos, incluindo números pequenos, médios e grandes. Aqui estão alguns resultados representativos:

### Números Pequenos

Testando: 4 × 5
Resultado: 20 ✓

Testando: 12 × 13
Resultado: 156 ✓


### Números Médios

Testando: 1234 × 5678
Resultado: 7006652 ✓

Testando: 9999 × 9999
Resultado: 99980001 ✓


### Números Grandes

Testando: 12345678 × 87654321
Resultado: 1082152022374638 ✓

Testando: 123456789 × 987654321
Resultado: 121932631112635269 ✓


### Casos Especiais

# Potências de 10
Testando: 1000 × 1000
Resultado: 1000000 ✓

# Números com zeros
Testando: 1002003 × 3002001
Resultado: 3008014008003 ✓


### Relatório de Precisão
- *Total de testes realizados:* 10
- *Testes bem-sucedidos:* 10
- *Taxa de precisão:* 100.00%

## Comparação com Multiplicação Tradicional

| Método | Complexidade | Eficiência para números grandes |
|--------|-------------|--------------------------------|
| Tradicional | O(n²) | Menor |
| Karatsuba | O(n^1.585) | Maior |

## Documentação e Links Úteis

- [Artigo Original de Karatsuba (1962)](https://link.springer.com/article/10.1007/BF01245642)
- [Análise Detalhada do Algoritmo](https://en.wikipedia.org/wiki/Karatsuba_algorithm)
- [Visualização do Algoritmo](https://www.youtube.com/watch?v=JCbZayFr9RE)

## Licença

Este projeto está licenciado sob a Licença MIT.
