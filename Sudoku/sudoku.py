import itertools

linhas = "123456789"
colunas = "ABCDEFGHI"

class Sudoku:

    def __init__(self, grelha):       # Inicializa os atributos
        
        self.celulas = list()         # Lista que contém as 81 variáveis do sudoku 
        self.celulas = self.gerar_coordenadas()

        self.possibilidades = dict()  # Dicionário que contém todas as possibilidades de cada célula
        self.possibilidades = self.gerar_possibilidades(grelha)
   
        self.regras_restricoes = self.gerar_regras_restricoes()  # Lista com todas as restrições

        self.restricoes_binarias = list() # Lista com todas as restrições binárias, com base na lista regras_restricoes
        self.restricoes_binarias = self.gerar_restricoes_binarias(self.regras_restricoes)

        self.celulas_vizinhas = dict() # Dicionário com todas as variáveis vizinhas de cada célula
        self.celulas_vizinhas = self.gerar_celulas_vizinhas()

    def gerar_coordenadas(self):       # Funcao para gerar as coordenadas do Sudoku

        total_coordenadas_celulas = []

        for coluna in colunas:

            for linha in linhas:
                
                novas_coordenadas = coluna + linha
                total_coordenadas_celulas.append(novas_coordenadas)

        return total_coordenadas_celulas

    def gerar_possibilidades(self, grelha):   # Função que gera todos os possíveis valores restantes para cada célula

        grelha_lista = list(grelha)

        possibilidades = dict()

        for index, coordenadas in enumerate(self.celulas):
            
            if grelha_lista[index] == "0":
                possibilidades[coordenadas] = list(range(1,10))
            
            else:
                possibilidades[coordenadas] = [int(grelha_lista[index])]

        return possibilidades

    def gerar_regras_restricoes(self):         # Funcao para gerar restricoes, com base nas regras do Sudoku
        
        restricoes_linha = []
        restricoes_coluna = []
        restricoes_quadrado = []

        for linha in linhas:
            restricoes_linha.append([coluna + linha for coluna in colunas])

        for coluna in colunas:
            restricoes_coluna.append([coluna + linha for linha in linhas])

        coordenadas_linhas_quadrado = (colunas[i:i+3] for i in range(0, len(linhas), 3))
        coordenadas_linhas_quadrado = list(coordenadas_linhas_quadrado)

        coordenadas_colunas_quadrado = (linhas[i:i+3] for i in range(0, len(colunas), 3))
        coordenadas_colunas_quadrado = list(coordenadas_colunas_quadrado)

        # Para cada quadrado
        for linha in coordenadas_linhas_quadrado:
            for coluna in coordenadas_colunas_quadrado:

                restricoes_quadrado_act = []
                
                # Para cada valor nesse quadrado
                for x in linha:
                    for y in coluna:
                        restricoes_quadrado_act.append(x + y)

                restricoes_quadrado.append(restricoes_quadrado_act)

        # As restricoes sao a soma destas 3 regras
        return restricoes_linha + restricoes_coluna + restricoes_quadrado

    def gerar_restricoes_binarias(self, regras_restricoes):   # Funcao para gerar retricoes binarias com base nas restricoes das regras do Sudoku
        restricoes_binarias_geradas = list()

        for restricoes in regras_restricoes:

            restricoes_binarias = list()

            for restricao_tupla in itertools.permutations(restricoes, 2):
                restricoes_binarias.append(restricao_tupla)

            for restricao in restricoes_binarias:

                restricao_lista = list(restricao)
                if(restricao_lista not in restricoes_binarias_geradas):
                    restricoes_binarias_geradas.append([restricao[0], restricao[1]])

        return restricoes_binarias_geradas

    def gerar_celulas_vizinhas(self): # Função que gera um dicionário em cada célula e contém todas as variáveis que possuem um relacionamento com essa célula
        celulas_vizinhas = dict()

        for celula in self.celulas:

            celulas_vizinhas[celula] = list()

            for restricao in self.restricoes_binarias:
                if celula == restricao[0]:
                    celulas_vizinhas[celula].append(restricao[1])

        return celulas_vizinhas

    def terminou(self):             # Função que verifica se a solução do sudoku está terminada
        for coordenadas, possibilidades in self.possibilidades.items():
            if len(possibilidades) > 1:
                return False
        
        return True
    
    def __str1__(self, matrix): # Funcao que imprime o Sudoku, inicialmente, na consola
        
        for i in range(len(matrix)):
            
            if i % 3 == 0 and i % 9 != 0:
                print("| ", end="")
            if i % 9 == 0 and i != 0:
                print("")
            if i % 27 == 0 and i != 0:
                print("- - - - - - - - - - -")
    
            for j in range(len(matrix[0])):
                
                print("\033[31m"  +str(matrix[i][j]) + " ", end="" + "\033[0;0m")
                    
                    
    def __str2__(self):        # Funcao que retorna o Sudoku resolvido

        resultado = ""
        contagem = 1
        
        for celula in self.celulas:

            valor = str(self.possibilidades[celula])
            if type(self.possibilidades[celula]) == list:
                valor = str(self.possibilidades[celula][0])

            if contagem % 3 == 0 and contagem % 9 != 0:
                resultado += "" + valor + " | " 
            elif(contagem % 3 == 0 and contagem % 9 == 0):
                resultado += "" + valor + "" 
            else:
                resultado += "" + valor + " "
            if contagem % 27 == 0 and contagem <= 70 :
                resultado +="\n- - - - - - - - - - -"
            if contagem % 9 == 0:
                resultado += "\n"
            
            contagem += 1
        
        return resultado