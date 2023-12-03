import numpy as np

def gerar_senha(num_cores, cores_disponiveis):
    if num_cores > len(cores_disponiveis):
        num_cores = len(cores_disponiveis)

    # Escolha aleatoriamente 'num_cores' cores da lista
    combinacao_cores = np.random.choice(cores_disponiveis, num_cores, replace=False)

    return list(combinacao_cores) 
def proximidade(tentativa, senha):
    resultado = []
    tentativa_copia = list(tentativa)  # Cópia da tentativa
    senha_copia = list(senha)          # Cópia da senha

    # Primeira iteração para identificar círculos brancos
    for i in range(len(tentativa)):
        if tentativa[i] == senha[i]:
            tentativa_copia[i] = None
            senha_copia[i] = None
            resultado.append("white")

    # Segunda iteração para identificar círculos cinzas
    for i in range(len(tentativa_copia)):
        if tentativa_copia[i] is not None and tentativa_copia[i] in senha_copia:
            senha_copia.remove(tentativa_copia[i])
            resultado.append("grey")

    # Terceira iteração para identificar círculos pretos
    for i in range(len(tentativa)):
        if tentativa[i] != senha[i]:
            resultado.append("black")

    return resultado

