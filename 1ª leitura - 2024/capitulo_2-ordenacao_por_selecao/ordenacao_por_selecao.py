# Função para encontra o menor elemento em um array

def buscaMenor(array):
    menor = array[0]
    menor_indice = 0
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_indice = i
    return menor_indice

# Ordenação por Seleção
def ordenacaoPorSelecao(array):
    novoArray = []
    for i in range(len(array)):
        menor = buscaMenor(array)
        novoArray.append(array.pop(menor))
    return novoArray

print(ordenacaoPorSelecao([5, 3, 6, 2, 10]))