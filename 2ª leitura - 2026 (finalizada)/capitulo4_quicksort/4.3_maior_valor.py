def maiorValor(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    maior_do_Resto = maiorValor(lista[1:])
    return lista[0] if lista[0] > maior_do_Resto else maior_do_Resto

print(maiorValor([3,5,2]))