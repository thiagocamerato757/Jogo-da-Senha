import numpy as np
from Lista_Generica import adicionaElementoLista
def gerar_senha(num_cores, cores_disponiveis):
    if num_cores > len(cores_disponiveis):
        num_cores = len(cores_disponiveis)

    # Escolha aleatoriamente 'num_cores' cores da lista
    combinacao_cores = np.random.choice(cores_disponiveis, num_cores, replace=False)

    return list(combinacao_cores) 
def proximidade(tentativa, senha):
    resultado = []

    # Cópias das listas
    tentativa_copia = list(tentativa)
    senha_copia = list(senha)

    # Primeira iteração para identificar círculos brancos
    for i in range(len(tentativa)):
        if tentativa[i] == senha[i]:
            adicionaElementoLista(resultado, "white")

    # Segunda iteração para identificar círculos cinzas
    for i in range(len(tentativa_copia)):
        if tentativa_copia[i] is not None and tentativa_copia[i] in senha_copia:
            senha_copia.remove(tentativa_copia[i])
            adicionaElementoLista(resultado, "grey")

    # Terceira iteração para identificar círculos pretos
    for i in range(len(tentativa)):
        if tentativa[i] != senha[i]:
            adicionaElementoLista(resultado, "black")

    # Garante que a lista de resultado tenha o tamanho correto (4 elementos)
    while len(resultado) < 4:
        adicionaElementoLista(resultado, "black")

    return resultado

