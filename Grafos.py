import networkx as nx # Biblioteca para manipulação de grafos
import matplotlib.pyplot as plt
import random
import math


#Grafos Aleatórios:

def criar_grafo_aleatorio(x):
    p = math.log(x) / x
    arestas = []

    for i in range(1, x + 1):
        for j in range(1, x + 1):
            if j > i:
                t = random.uniform(0, 1)
                if t > 1 - p:
                    arestas.append((i, j))

    # Funções para criar um grafo não-direcionado e adicionar as arestas que estão na lista:
    grafo = nx.Graph()
    grafo.add_edges_from(arestas)
    
    # Definição de layout(existem outros tipos):
    pos = nx.spring_layout(grafo)
    
    plt.figure(1)
    plt.title('Grafo Aleatório')
    nx.draw(grafo, pos, with_labels=True)
    plt.show()

    # Calcular o diâmetro:
    diametro = nx.diameter(grafo)
    print(f"Diâmetro do Grafo Aleatório: {diametro}")



# Grafos Heterogêneos:

def criar_grafo_heterogeneo(x):
    arestas = []
    L = [1, 2]
    arestas.append((1, 2))

    for i in range(3, x + 1):
        u = random.choice(L)
        arestas.append((i, u))
        L.extend([u, i])

    # Funções para criar um grafo não-direcionado e adicionar as arestas que estão na lista:
    grafo = nx.Graph()
    grafo.add_edges_from(arestas)

    # Definição de layout(existem outros tipos):
    pos = nx.kamada_kawai_layout(grafo)
    
    plt.figure(2)
    plt.title("Grafo Heterogêneo")
    nx.draw(grafo, pos, with_labels=True)
    plt.show()

    # Calcular Diâmetro:
    diametro = nx.diameter(grafo)
    print(f"Diâmetro do Grafo Heterogêneo: {diametro}")

# Código principal que se inicia com redes de tamanho igual a 100

c = 100
    
criar_grafo_aleatorio(c)
criar_grafo_heterogeneo(c)



