def pesquisa_binaria(lista, item):
    baixo = 0 # menor posicao
    alto = len(lista) - 1 # maior posicao

    cont = 1

    while baixo <= alto: # enquanto nao chegar a um unico elemento
        # verifica o elemento central
        meio = (baixo + alto) // 2 # arredondado automaticamente para baixo pelo python
        chute = lista[meio]
        print("Iteração",cont)
        print("----------")
        print("- baixo:",baixo)
        print("- alto:",alto)
        print("- meio:",meio)
        print("- chute:",chute)
        print("- valor procurado:",item)
        print()

        if chute == item:
            return meio
        if chute > item: 
            alto = meio - 1 # se o chute for muito alto, atualiza a variavel alto
        else:
            baixo = meio + 1 # se o chute for muito baixo, atualiza a variavel baixo
        cont += 1
    return None

minha_lista = [1,3,5,7,9]
print(pesquisa_binaria(minha_lista, 3)) # => 1