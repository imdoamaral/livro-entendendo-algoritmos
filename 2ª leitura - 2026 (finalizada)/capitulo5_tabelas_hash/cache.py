# Demonstração de Utilização de tabelas hash como cache
cache = {}

def pega_pagina(url):
    if cache.get(url):
        return cache(url)  # Retorna os dados do cache
    else:
        dados = pega_dados_do_servidor(url)
        cache[url] = dados  # Salva esses dados primeiro no seu cache
        return dados
