import sys

# Encontra caminho hamiltoniano para grafo usando backtracking
# Complexidade de tempo: O(V!)
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
     
# Encontra um caminho hamiltoniano num grafo direcionado usando backtracking
# Complexidade de tempo: O(V!) (por usar o backtracking)
def solve_it(graph):
    res = []
    backtracking(res, graph, [0], set([0]), 0)
    
    # Retorna caminho hamiltoniano
    return res

# Verifica se a solução dada é válida
# Complexidade de tempo: O(n)
def verify_it(sol, graph):
    # Verifica se a solução possui o mesmo tamanho que o grafo (Não houve uma "volta" a um nó)
    if len(sol) != len(graph):
        return False
    
    # Remove duplicatas (se houverem) e verifica se a solução continua possuindo a quantidade certa de elementos
    if len(set(sol)) != len(graph):
        return False
    
    # Itera sobre a solução, conferindo se há conexão entre um nó com seu antecessor
    for i in range(1, len(sol)):
        u, v = sol[i - 1], sol[i] 
        if(v not in graph[u]):
            return False
        
    return True;

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        lines = input_data.strip().split('\n')
    
        # Lê número de vértices e arestas
        V, E = map(int, lines[0].split())
        
        # Inicializa a lista de adjacência
        adj_list = [[] for _ in range(V)]
        
        # Processa cada aresta
        for line in lines[1:]:
            u, v = map(int, line.split())
            adj_list[u].append(v)

        # Output
        sol = solve_it(adj_list)
        print(f"Grafo: {adj_list}")
        print(f"Solução: {sol}")
        print(f"A solução é válida" if verify_it(sol, adj_list) else "Solução inválida")
    else:
        print('Este teste exige um input válido, selecione um dos exemplos disponíveis (e.g. ./data/graph_2_1)')
