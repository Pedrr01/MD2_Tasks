import networkx as nx # Biblioteca usada para manipulação e análise de redes
import matplotlib.pyplot as plt

def dijkstra(grafo, origem):
    distancias = {node: float('inf') for node in grafo}
    predecessores = {node: None for node in grafo}
    distancias[origem] = 0

    Q = set(grafo)

    # Algoritmo de Dijkstra
    while Q:
        vertice_atual = min(Q, key=lambda node: distancias[node])
        Q.remove(vertice_atual)

        for vizinho, peso in grafo[vertice_atual].items():
            alt = distancias[vertice_atual] + peso
            if alt < distancias[vizinho]:
                distancias[vizinho] = alt
                predecessores[vizinho] = vertice_atual

    for node in grafo:
        if predecessores[node] is None:
            predecessores[node] = node

    return distancias, predecessores

def melhor_caminho(predecessores, origem, chegada):
    caminho = []
    atual = chegada
    while atual != origem:
        caminho.insert(0, atual)
        atual = predecessores[atual]
    caminho.insert(0, origem)
    return caminho

# Grafo representado como um dicionário de dicionários
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 1, 'D': 3, 'E': 5},
    'C': {'A': 4, 'B': 1, 'D': 2, 'E': 3},
    'D': {'B': 3, 'C': 2, 'E': 2},
    'E': {'B': 5, 'C': 3, 'D': 2}
}

# Escolha do vértice de origem e chegada:
origem = 'A'
chegada = 'E'

distancias, predecessores = dijkstra(grafo, origem)
print("Distâncias a partir de", origem + ":", distancias)
print("Predecessores:", predecessores)

caminho = melhor_caminho(predecessores, origem, chegada)
print("Melhor caminho de", origem, "para", chegada + ":", caminho)

# Plotar o grafo:
G = nx.Graph()
for node in grafo:
    for vizinho, peso in grafo[node].items():
        G.add_edge(node, vizinho, weight=peso)

pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)
plt.title("Grafo - Algoritmo de Dijkstra")
plt.show()
