def quicksort(array):
    if len(array) < 2:
        return array  # Caso base: arrays com 0 ou 1 elementos já estão "ordenados"
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]  # subarray de todos os elementos menores que o pivô
        maiores = [i for i in array[1:] if i > pivo]  # subarray de todos os elementos maiores que o pivô
        return quicksort(menores) + [pivo] + quicksort(maiores)  # retorna a concatenação de 3 listas


print(quicksort([10, 5, 2, 3]))
