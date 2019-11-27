import sys


# Classe que define um Grafo aresta ponderado
class Graph:

    # Construtor da classe
    # Recebe o número de vértices do grafo
    def __init__(self, vertices):
        self.vertices = vertices  # Salva a quantidade de vertices
        self.graph = [[-1 for c in range(0, vertices)] for r in
                      range(0, vertices)]  # Cria a matriz de adjacencia do grafo

    # Função que calula a árvore geradora mínima
    def prim_tree(self):
        parents = [None] * self.vertices  # Vetor que guarda os predecessores
        costs = [sys.maxsize] * self.vertices  # Vetor para cálculo dos custos dos caminhos até os vértices
        in_tree = [False] * self.vertices  # Vetor para indicar se o vértice já foi incluído na árvore

        # Define o primeiro vértice a ser incluído na árvore
        parents[0] = -1
        costs[0] = 0

        # Para cada vértice do grafo
        for _ in range(0, self.vertices):
            min_cost = sys.maxsize  # Varíavel para controle do menor custo partindo do vértice
            u = -1  # Indíce do vértice de menor custo

            # Para cada vértice do grafo
            for v in range(0, self.vertices):
                # Se o custo para chegar a este vértice é menor do que o salvo atualmente e o vértice não está na árvore
                if costs[v] < min_cost and not in_tree[v]:
                    min_cost = costs[v]  # Atualiza o custo mínimo
                    u = v  # Atualiza o índice do menor custo

            # Indica que o vértive com menor custo foi colocado na árvore
            in_tree[u] = True

            # Para cada vértice do grafo
            for v in range(0, self.vertices):
                # Se existir aresta entre u e v, o custo dela for menor que o salvo atualmente e v não estiver na árvore
                if -1 < self.graph[u][v] < costs[v] and not in_tree[v]:
                    costs[v] = self.graph[u][v]  # Atualiza o custo para chegar a v
                    parents[v] = u  # Atualiza o predecessor de v

        # Retorna o vetor de predecessores
        return parents

    def print(self):
        for u in range(0, self.vertices):
            for v in range(0, self.vertices):
                print('{:5}'.format(self.graph[u][v]), end=' ')
            print('')

    def print_prim(self, parent):
        print("Edge   \tWeight")
        for i in range(1, self.vertices):
            print('{:>2} - {:<2}\t{:>6}'.format(parent[i], i, self.graph[i][parent[i]]))


# Função que executa o código
def main():
    # Faz a leitura do tamanho do grafo
    graph_size = int(input())

    # Se for um grafo vazio encerra o programa
    if graph_size == 0:
        sys.exit()

    graph = Graph(graph_size)  # Cria o grafo

    # Lê a matriz de adjacência do grafo
    for i in range(0, graph_size):
        edges = [int(x) for x in input().split(' ')]
        graph.graph[i] = edges

    # Calcula a árvore geradora mínima do grafo
    parents = graph.prim_tree()

    # Vetor para os custos da árvore mínima
    costs = [0] * graph_size

    # Busca no grafo o custo de todas as arestas e salva no vetor de custos
    for i in range(0, graph_size):
        costs[i] = graph.graph[i][parents[i]]

        if parents[i] == -1:
            costs[i] = 0

    # Remove a aresta de maior peso da árvore geradora mínima gerando a bifloresta geradora mínima
    costs[costs.index(max(costs))] = 0

    # Imprime o custo total da bifloresta geradora mínima
    print(sum(costs))


if __name__ == '__main__':
    main()
