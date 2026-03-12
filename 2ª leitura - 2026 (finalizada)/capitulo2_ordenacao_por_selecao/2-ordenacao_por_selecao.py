# Primeiro, vamos escrever uma funcao para encontrar o menor elemento num array:
def buscaMenor(arr):
    menor = arr[0] # armazena o menor valor
    menor_indice = 0 # armazena o indice do menor valor

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

# Agora, a funcao para a ORDENACAO POR SELECAO:
def ordenacaoPorSelecao(arr):
    novoArr = []

    for i in range(len(arr)):
        menor = buscaMenor(arr) # encontra o menor elemento do array e add ao novo array
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoPorSelecao([5,3,6,2,10]))