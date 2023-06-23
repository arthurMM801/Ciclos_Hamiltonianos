
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

# Teema de Ore
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


# Teorema de Bondy and Chvátal
# Será Hamiltoniano se o Fecho Hamiltoniano G for um grafo completo.

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



# verifica o resultado do ciclo nos tres metodos
def verificaH(grafo):
    print("Teorema de Dirac: ", verificaDirac(grafo))
    print("Teorema de ore: ", verificaOre(grafo))
    print("Teorema de Bondy & Chvátal: ", verificaB_e_C(grafo))
