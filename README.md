# Caminho Hamiltoniano e problema NP

Este repositório tem como objetivo mostrar que o problema do Caminho Hamiltoniano está no conjunto dos problemas NP. Para isso, apresentamos:

1. Um **verificador** que, dado um caminho proposto, confirma em tempo polinomial se ele é um caminho hamiltoniano válido em um grafo direcionado.
2. Um **algoritmo de busca** por caminho hamiltoniano usando backtracking, que ilustra a natureza exponencial do problema.

## 1. Conceituação

### 1.1 Caminho Hamiltoniano

Um **caminho hamiltoniano** em um grafo dirigido $G = (V, E)$ é um caminho simples que visita cada vértice exatamente uma vez. Formulamos dois desafios:

* **Verificação**: dado um grafo e um caminho candidato, determinar se ele é hamiltoniano.
* **Busca**: encontrar um caminho hamiltoniano em $G$, caso exista.

### 1.2 Classes de Complexidade

* **P**: problemas que podem ser resolvidos em tempo polinomial, i.e. $O(n^k)$ para alguma constante $k$.
* **NP**: problemas cujas soluções, uma vez fornecidas, podem ser **verificadas** em tempo polinomial, mas para os quais não se conhece algoritmo de resolução em tempo polinomial.

> **Proposição**: O problema do caminho hamiltoniano está em NP, pois podemos construir um verificador polinomial.

## 2. Verificador em tempo polinomial

O código abaixo implementa `verify_it(sol, graph)`, que recebe:

* `sol`: lista de vértices propostos na ordem do caminho.
* `graph`: lista de adjacência do grafo, em que `graph[u]` é a lista de vizinhos de `u`.

E verifica:

1. `len(sol) == len(graph)`: o caminho tem exatamente $|V|$ vértices.
2. `len(set(sol)) == len(graph)`: não há vértices repetidos.
3. Para cada par de vértices consecutivos $(u, v)$ em `sol`, existe uma aresta $u \rightarrow v$.

```py
def verify_it(sol, graph):
    if len(sol) != len(graph):
        return False

    if len(set(sol)) != len(graph):
        return False
    
    for i in range(1, len(sol)):
        u, v = sol[i-1], sol[i]
        if v not in graph[u]:
            return False
    
    return True
```

Esse algoritmo realiza um número de operações que cresce, no máximo, linearmente com o número de vértices e arestas — ou seja, em tempo polinomial. Logo, **a verificação de um caminho hamiltoniano está em P**, e o problema pertence a NP.

## 3. Busca via Backtracking

Para ilustrar a dificuldade de resolver o problema em geral, implementamos um algoritmo de backtracking que busca um caminho recursivamente, tentando todas as opções:

```py
def backtracking(res, graph, path, visited, node):
    if(len(path) == len(graph)):
        res.extend(path);
        return True;
    
    for neighbour in graph[node]:
        if(neighbour not in visited):
            visited.add(neighbour)
            path.append(neighbour)
            if backtracking(res, graph, path, visited, neighbour):
                return True
            visited.remove(neighbour)
            path.pop()
    
    return False;


def solve_it(graph):
    res = []
    backtracking(res, graph, [0], {0}, 0)
    return res
```

* **Entrada**: `graph` é a lista de adjacência.
* **Saída**: uma lista `res` com um caminho hamiltoniano se existir, ou lista vazia caso contrário.

Em um grafo completo de $V$ vértices, o algoritmo explora até $V!$ permutações, demonstrando a natureza pelo menos **exponencial** do problema (nesse caso, a solução tem complexidade fatorial).

## 4. Estrutura de I/O do Programa

### Input

```
<V> <E>
u_1 v_1
u_2 v_2
...
u_E v_E
```

* `<V>`: número de vértices.
* `<E>`: número de arestas.
* Em cada linha seguinte, aresta direcionada de `u_i` para `v_i`.

### Output

1. Lista de adjacência do grafo.
2. Caminho hamiltoniano encontrado (ou lista vazia).
3. Resultado da verificação (`válido` / `inválido`).

## 5. Conclusão

O problema de encontrar um caminho hamiltoniano é **NP**, pois, embora não conheçamos algoritmo polinomial para resolvê-lo em todos os casos, conseguimos **verificar** qualquer caminho candidato em tempo polinomial. A busca exaustiva por backtracking reforça sua complexidade exponencial no pior caso. 

Cabe ressaltar a existência de algoritmos capazes de determinar se um grafo possui um Caminho Hamiltoniano com uma complexidade inferior que $O(V!)$, como é o caso do Algoritmo de Bellman, Held, and Karp, sem, entretanto, encontrar esse caminho. A abordagem anterior, usa de programação e possui complexidade $O(2^n \cdot n^2)$, mais uma vez, destacando a dificuldade do problema.

## Bônus

Experimente testar o código com as entradas fornecidas na pasta [`data`](./data/). Para tal, basta executar com o seguinte comando:
```bash
python src,py ./data/[nome_do_arquivo]
```

Por exemplo:
```bash
python src,py ./data/graph_4_12
```

A seguir, uma estimativa de quanto tempo o algoritmo leva para gerar os resultados:

| Input  | Filename          | Estimativa de tempo  |
| :----: | :---------------- | :------------------: |
| **1**  | graph_4_12.txt    |        ~0,1 ms       |
| **2**  | graph_5_4.txt     |        ~0,05 ms      |
| **3**  | graph_6_6.txt     |        ~0,1 ms       |
| **4**  | graph_7_10.txt    |         ~5 ms        |
| **5**  | graph_8_20.txt    |        ~100 ms       |
| **6**  | graph_9_30.txt    |          ~1 s        |
| **7**  | graph_11_110.txt  |        ~7 minutos    |
| **8**  | graph_12_132.txt  |        ~1,6 horas    |
| **9**  | graph_14_182.txt  |        ~14 dias      |
| **10** | graph_16_240.txt  |        ~9,5 anos     |

## Referências

1. CORMEN, Thomas H. et al. *Algoritmos: teoria e prática*. 4. ed. Rio de Janeiro: GEN LTC, 2024. ISBN 9788595159914.

2. *Hamiltonian Path Tutorials & Notes | Algorithms*. HackerEarth. Disponível em: [https://www.hackerearth.com/practice/algorithms/graphs/hamiltonian-path/tutorial/](https://www.hackerearth.com/practice/algorithms/graphs/hamiltonian-path/tutorial/).
