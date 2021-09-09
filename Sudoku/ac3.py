def AC3(csp, queue=None):           # Método que aplica o algoritmo do AC3

    if queue == None:
        queue = list(csp.restricoes_binarias)

    while queue:

        (xi, xj) = remover_primeiro(queue)

        if rever(csp, xi, xj): 
            # Se uma célula tiver 0 possibilidades, o sudoku não tem solução
            if len(csp.possibilidades[xi]) == 0:
                return False
            
            for Xk in csp.celulas_vizinhas[xi]:
                if Xk != xi:
                    queue.append((Xk, xi))
                
    return True

def rever(csp, celula_i, celula_j):   # Função que verifica se as variáveis de um arco possuem valores iguais

    removido = False

    for valor in csp.possibilidades[celula_i]:

        if not any([diferente(valor, possibilidade) for possibilidade in csp.possibilidades[celula_j]]):
            
            csp.possibilidades[celula_i].remove(valor)
            removido = True
   
    return removido

def remover_primeiro(queue):   # Função que elimina o elemento que se está no topo da queue
    return queue.pop(0)

def diferente(cell_i, cell_j): # Função que verifica se as variáveis de um arco são diferentes
    result = cell_i != cell_j
    return result