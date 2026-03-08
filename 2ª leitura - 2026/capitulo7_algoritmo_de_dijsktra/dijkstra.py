grafo = {}
custos = {}
pais = {}
processados = []

def ache_nodo_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None

    for nodo in custos:  # Vá por cada vértice
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:  # Se for o vértice de menor custo até o momento e ele ainda não tiver sido processado...
            custo_mais_baixo = custo  # ... atribua como o novo vértice de menor custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = ache_nodo_custo_mais_baixo(custos)  # Encontra o custo mais baixo que ainda não foi processado
while nodo is not None:  # Caso todos os vértices tenham sido processados, esse laço while será finalizado
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():  # Percorre todos os vizinhos desse vértice
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:  # Caso seja mais barato chegar a um vizinho a partir desse vértice...
            custos[n] = novo_custo  # ... atualiza o custo dele.
            pais[n] = nodo  # Esse vértice se torna o novo pai para o vizinho
    processados.append(nodo)  # Marca o vértice como processado
    nodo = ache_nodo_custo_mais_baixo(custos)  # Encontra o próximo vértice a ser processado e o algoritmo é repetido
