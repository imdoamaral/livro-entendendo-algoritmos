def contaItens(lista):
    if lista == []:
        return 0

    total = 0
    # for i in lista:
    #     total += 1
    # return total

    return 1 + contaItens(lista[1:])

print(contaItens([1, 2, 3]))  #
