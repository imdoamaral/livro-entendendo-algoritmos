# def encontra_maior_valor(lista):
#     if not lista:
#         return None
#     return max(lista)

# print(encontra_maior_valor([5, 2, 7, 3, 6]))

def encontra_maior_valor_recursivo(lista):
    if not lista:
        return 0
    else:
        maior_do_resto = encontra_maior_valor_recursivo(lista[1:])

        if lista[0] > maior_do_resto:
            return lista[0]
        else:
            return maior_do_resto
        
print(encontra_maior_valor_recursivo([5, 2, 7, 3, 6]))