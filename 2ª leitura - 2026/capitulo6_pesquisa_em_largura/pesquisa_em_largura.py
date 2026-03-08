from collections import deque

grafo = {}

def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print("É um vendedor!")
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    return False


pesquisa("voce")
