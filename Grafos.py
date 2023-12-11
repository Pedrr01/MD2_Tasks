import random
import networkx as nx #Bibliotecas para manipulação de grafos
import matplotlib.pyplot as plt
import math

#Grafos Aleatórios:

def grafoAl(x):
    p = math.log(x) / x
    arestas = []

    for i in range(1, x + 1):
        for j in range(1, x + 1):
            if i < j:
                t = random.uniform(0, 1)
                if t > 1 - p:
                    arestas.append((i, j))

    #Funções para criar um grafo não-direcionado e adicionar as arestas que estão na lista:
    G = nx.Graph()
    G.add_edges_from(arestas)

    #Definição de layout(existem outros tipos):
    layout = nx.spring_layout(G)  

    plt.figure(1)
    plt.title('Grafo Aleatório')
    nx.draw(G, pos=layout, with_labels=True)
    plt.show()

    diametro = nx.diameter(G)
    return G, diametro

n = 100
grafo_al, diametro_al = grafoAl(n)



# Grafos Heterogêneos:

def grafoHet(x):
    arestas = []
    L = [1, 2]
    arestas.append((1, 2))

    for i in range(3, x + 1):
        u = random.choice(L)
        arestas.append((i, u))
        L.extend([u, i])

    #Funções para cria um grafo não-direcionado e adicionar as arestas que estão na lista:
    G = nx.Graph()
    G.add_edges_from(arestas)

    #Definição de layout(existem outros tipos):
    layout = nx.kamada_kawai_layout(G)

    plt.figure(2)
    plt.title('Grafo Heterogêneo')
    nx.draw(G, pos=layout, with_labels=True)
    plt.show()

    diametro = nx.diameter(G)
    return G, diametro

n = 100
grafo_het, diametro_het = grafoHet(n)

