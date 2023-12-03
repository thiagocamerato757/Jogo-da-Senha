import numpy as np

def gerar_senha(num_cores, cores_disponiveis):
    if num_cores > len(cores_disponiveis):
        num_cores = len(cores_disponiveis)

    # Escolha aleatoriamente 'num_cores' cores da lista
    combinacao_cores = np.random.choice(cores_disponiveis, num_cores, replace=False)

    return combinacao_cores
#Todo: incluir esssa funcao na partida 
def proximidade(tentativa, senha):
    resultado = []
    i = 0
    while i < len(tentativa):
        if tentativa[i] == senha[i]:
            del tentativa[i]
            del senha[i]
            resultado.append("white")
        i += 1
    for el in tentativa:
        if el in senha:
            senha.remove(el)
            resultado.append("grey")
    i = 0
    while len(resultado) < 4:
        resultado.append("black")
    return resultado
