import random


# Teorema de euler

# É euleriano se se somente se todos os seus vertices possuírem grau par
def euleriano(grafo):
    for i in range(len(grafo)):
        if (len(grafo[i]) % 2) != 0:
            return False
    return True

# É semi-euleriano se possuir dois vertices de grau impar
def semiEuleriano(grafo):
    impares = 0
    for i in range(len(grafo)):
        if (len(grafo[i]) % 2) != 0:
            impares += 1
    if impares == 2:
        return True
    return False

# Não é euleriano se posuir mais de dois vertices de grau impar
def naoEuleriano(grafo):
    impares = 0
    for i in range(len(grafo)):
        if ((len(grafo[i]) % 2) != 0) and impares < 2:
            impares += 1
    if impares >= 2:
        return True
    return False

def tipoCicloEuleriano(grafo):
    if euleriano(grafo):
        return "Euleriano"
    if semiEuleriano(grafo):
        return "Semi-Euleriano"
    return "Não Euleriano"

def  grafoVazio(grafo):
    for i in range(len(grafo)):
        if len(grafo[i]) != 0:
            return False
    return True


# Caminho Euleriano

# Verifica se o proximo caminho é possivel
def caminhoPossivel(vertice, proximoVertice, grafo):
    if (len(grafo[vertice]) > 1 and len(grafo[proximoVertice]) == 1):
        return False
    return True


# funcção recurciva que vai criar o caminho
def proximoCaminho(vertice, caminho, grafo):
    # print(grafo)
    for i in grafo[vertice]:
        proximoVertice = i  # Escolhe o proximo vertice do caminho
        if not caminhoPossivel(vertice, proximoVertice, grafo):
            continue
        caminho.append(proximoVertice)  # Adicionao proximo vertice ao caminho
        grafo[vertice].remove(proximoVertice)  # Remove a aresta que passou
        grafo[proximoVertice].remove(vertice)
        # print(caminho)
        return proximoCaminho(proximoVertice, caminho, grafo)
    return caminho

def caminhoEuleriano(inicio, grafo):
    tipo = tipoCicloEuleriano(grafo)
    if tipo == "Euleriano" or tipo == "Semi-Euleriano":
        caminhoEuleriano = [inicio]
        caminhoEuleriano = proximoCaminho(inicio, caminhoEuleriano, grafo)
        # print(caminhoEuleriano)
        return caminhoEuleriano
    return "Grafo não Euleriano! Caminho impossível."



# Cria uma matriz com pesos aleatorios para testar o caminho euleriano
def transformaMatriz(grafo):
    size = len(grafo)
    matriz = [[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in grafo[i]:
            if matriz[i][j] == 0:
                peso = random.randrange(1, 10)
                matriz[i][j] = peso
                matriz[j][i] = peso
    return matriz

# Retorna o valor do caminho total
# com base no caminho euleriano de um grafo
def somaCaminho(grafo, caminho):
    soma = 0
    i = 1
    while i < len(caminho):
        atual = caminho[i-1]
        proximo = caminho[i]
        # print(soma)
        soma += grafo[atual][proximo]
        i += 1
    return soma



# Verifica o resultado do caminho euelriano
def verificaE(ciclo, vertice):
    # Copia do ciclo
    cicloTeste = ciclo.copy()

    tipo = tipoCicloEuleriano(cicloTeste)
    print("Tipo: ", tipo)
    if tipo == 'Não Euleriano':
        print()
        return

    matriz = transformaMatriz(cicloTeste)
    for i in matriz:
        print(i)

    caminho = caminhoEuleriano(vertice, cicloTeste)
    print("Caminho: ", caminho)
    print("Soma = ", somaCaminho(matriz, caminho))
    print()
