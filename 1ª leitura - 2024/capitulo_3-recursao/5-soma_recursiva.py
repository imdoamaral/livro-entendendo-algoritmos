# def soma(lista):
#     total = 0
#     for valor in lista:
#         total += valor
#     return total

# print(soma([2, 4, 6]))

def soma_recursiva(lista):
    # Caso base: se a lista estiver vazia, retorna 0
    if not lista:
        return 0
    # Passo recursivo: soma o primeiro elemento da lista com o resultado da soma do restante da lista
    else:
        return lista[0] + soma_recursiva(lista[1:])
    
print(soma_recursiva([2, 4, 6]))