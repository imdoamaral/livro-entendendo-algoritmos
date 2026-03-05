# Soma padrão
def soma(lista):
    total = 0
    for x in lista:
        total += x
    return total


print(soma([1, 2, 3, 4]))

# Soma recursiva
def somaRecursiva(lista):
    total = 0
    if lista == []:
        return 0

    return lista[0] + somaRecursiva(lista[1:])


print(somaRecursiva([1, 2, 3]))  # 1 + ([2,3])
