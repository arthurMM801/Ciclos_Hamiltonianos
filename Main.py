ciclo1 = [
    [1, 2, 5, 6],  # Vertice 0
    [0, 2, 3, 5],  # Vertice 1
    [0, 1, 3, 4],  # Vertice 2
    [1, 2, 4, 6],  # Vertice 3
    [2, 3, 5, 6],  # Vertice 4
    [0, 1, 4, 6],  # Vertice 5
    [0, 3, 4, 5],  # Vertice 6
]

ciclo2 = [
    [1, 2, 5, 6],  # Vertice 0
    [0, 2, 3, 5],  # Vertice 1
    [0, 1, 3],     # Vertice 2
    [1, 2, 4, 6],  # Vertice 3
    [3, 5, 6],     # Vertice 4
    [0, 1, 4, 6],  # Vertice 5
    [0, 3, 4, 5],  # Vertice 6
]

ciclo3 = [
    [1, 2, 5, 6],  # Vertice 0
    [0, 2],        # Vertice 1
    [0, 1, 3],     # Vertice 2
    [2, 4],        # Vertice 3
    [3, 5, 6],     # Vertice 4
    [0, 4, 6],     # Vertice 5
    [0, 4, 5],     # Vertice 6
]

ciclo4 = [
    [1, 2, 5, 6],  # Vertice 0
    [0, 2],        # Vertice 1
    [0, 1, 3],     # Vertice 2
    [2, 4],        # Vertice 3
    [3, 5],        # Vertice 4
    [0, 4, 6],     # Vertice 5
    [0, 5],        # Vertice 6
]


# Teorema de Dirac
# Seja G um grafo simples com n vértices, onde n ≥ 3.
# Seja d(x) o grau do vertice x. Se d(v) ≥ n/2,
# para cada vértice v, então G é hamiltoniano.

def verificaDirac(grafo):
    # Caso numero de vercites >=3
    if len(grafo) < 2:
        return False
    # Itera sobre os vertices do ciclo
    for i in range(len(grafo)):
        # ! ( d(v) ≥ n/2 )
        if not len(grafo[i]) >= len(grafo) / 2:
            return False
    return True


# Seja G um grafo simples com n vértices, onde n ≥ 3.
# Seja d(x) o grau do vertice x. Se d(v) + d(w) ≥ n,
# para qualquer par de vértices não adjacentes v e w,
# então G á hamiltoniano.

def verificaOre(grafo):
    # Itera sobre os vertices do ciclo e verifica os adjacentes para cada
    for i in range(len(grafo)):
        for j in range(len(grafo)):
            # Caso vertices não adjacentes
            if i != j and j not in grafo[i]:
                # Caso soma dos graus não for >= quantidade de vertices
                if not len(grafo[i]) + len(grafo[j]) >= len(grafo):
                    return False
    return True


def fechoHamiltoniano(grafo):
    fecho = grafo
    i = 0
    j = 0
    # Itera sobre os vertices do ciclo e verifica os adjacentes para cada
    while i < len(grafo):
        while j < len(grafo):
            # Caso vertices não adjacentes e a soma dos graus >= quantidade de vertices
            if i != j and j not in fecho[i] and len(fecho[i]) + len(fecho[j]) >= len(fecho):
                # Cria uma arenta entre os vertices
                fecho[i].append(j)
                fecho[j].append(i)
                i = j = 0
            j += 1
        j = 0
        i += 1
    return fecho

def vericaGrafoCompleto(grafo):
    for i in range(len(grafo)):
        if not len(grafo[i]) == (len(grafo) - 1):
            return False
    return True

def verificaB_e_C(grafo):
    return vericaGrafoCompleto(fechoHamiltoniano(grafo))



print("Teorema de Dirac")
print("Ciclo 1: ", verificaDirac(ciclo1))
print("Ciclo 2: ", verificaDirac(ciclo2))
print("Ciclo 3: ", verificaDirac(ciclo3))
print("Ciclo 4: ", verificaDirac(ciclo4))
print()

print("Teorema de ore")
print("Ciclo 1: ", verificaOre(ciclo1))
print("Ciclo 2: ", verificaOre(ciclo2))
print("Ciclo 3: ", verificaOre(ciclo3))
print("Ciclo 4: ", verificaOre(ciclo4))
print()

print("Teorema de Bondy & Chvátal ")
print("Ciclo 1: ", verificaB_e_C(ciclo1))
print("Ciclo 2: ", verificaB_e_C(ciclo2))
print("Ciclo 3: ", verificaB_e_C(ciclo3))
print("Ciclo 4: ", verificaB_e_C(ciclo4))
