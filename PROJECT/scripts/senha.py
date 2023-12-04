import numpy as np
from Lista_Generica import adicionaElementoLista
def gerar_senha(num_cores, cores_disponiveis):
    if num_cores > len(cores_disponiveis):
        num_cores = len(cores_disponiveis)

    # Escolha aleatoriamente 'num_cores' cores da lista
    combinacao_cores = np.random.choice(cores_disponiveis, num_cores, replace=True)

    return list(combinacao_cores) 

def proximidade(tentativa, senha):
    resultado = []

    # Cópias das listas
    tentativa_copia = list(tentativa)
    senha_copia = list(senha)

    # Primeira iteração para identificar círculos brancos
    i = 0
    while i < len(tentativa_copia):
        if tentativa_copia[i] == senha_copia[i]:
            del tentativa_copia[i]
            del senha_copia[i]
            adicionaElementoLista(resultado, "white")
        else:
            i += 1

    # Segunda iteração para identificar círculos cinzas
    for el in tentativa_copia:
        if el in senha_copia:
            senha_copia.remove(el)
            adicionaElementoLista(resultado, "grey")

    # Terceira iteração para preencher os círculos pretos
    while len(resultado) < 4:
        adicionaElementoLista(resultado, "black")

    return resultado
