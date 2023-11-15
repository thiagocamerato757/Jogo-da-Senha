import numpy as np

def gerar_senha(num_cores, cores_disponiveis):
    if num_cores > len(cores_disponiveis):
        num_cores = len(cores_disponiveis)

    # Escolha aleatoriamente 'num_cores' cores da lista
    combinacao_cores = np.random.choice(cores_disponiveis, num_cores, replace=False)

    return combinacao_cores
