votaram = {}

def verifica_eleitor(nome):
    if votaram.get(nome):
        print("Mande embora!")
    else:
        votaram[nome] = True
        print("Deixe votar!")


print(verifica_eleitor("Tom"))
print(verifica_eleitor("Mike"))
print(verifica_eleitor("Mike"))
