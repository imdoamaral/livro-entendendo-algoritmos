# def conta_itens(lista):
#     return len(lista)
# print(conta_itens([1, 2, 3, 4]))

def conta_itens_recursiva(lista):
    if not lista:
        return 0
    else:
        return 1 + conta_itens_recursiva(lista[1:])
    
print(conta_itens_recursiva([1, 2, 3, 4]))