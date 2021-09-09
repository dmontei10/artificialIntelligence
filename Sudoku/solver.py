import sys              # Bibliotecas de suporte à execução do programa
from sudoku import Sudoku
from ac3 import AC3
import time
from random import sample
 
base  = 3
lado  = base * base

def criar_sudoku():     # Função que gera um sudoku aleatório
    
    def padrao(r,c): 
        return (base * (r % base) + r//base + c) % lado
    
    def baralhar(s): 
        return sample(s,len(s)) 
    
    rBase = range(base) 
    linhas  = [ g*base + r for g in baralhar(rBase) for r in baralhar(rBase) ] 
    colunas  = [ g*base + c for g in baralhar(rBase) for c in baralhar(rBase) ]
    nums  = baralhar(range(1,base*base+1))
    
    board = [ [nums[padrao(r,c)] for c in colunas] for r in linhas ]
    
    quadrados = lado * lado
    vazios = quadrados * 3//6
    for p in sample(range(quadrados),vazios):
        board[p//lado][p%lado] = 0
    
    normal = [val for line in board for val in line]
    converterStr = ''.join(map(str, normal)) 
    
    return converterStr

sudoku = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
sudoku_aleat = criar_sudoku()

value = list()
value2 = list()

timeCount = 0


def solve(grid, index, total):   # Função para resolver o sudoku proposto, com a implementação do algoritmo de AC-3
        
    inicio = time.time()
        
    sudoku = Sudoku(grid)    
    
    print("\n       Sudoku       \n")
    print("{}".format(sudoku.__str1__(grid)))
        
    print("\nAC3 iniciou")
        
    AC3_result = AC3(sudoku)
    
    if not AC3_result:
        print("\nEste Sudoku não tem solução")
    
    else:
            
        if sudoku.terminou():
    
            print("\n\033[32mAC3 é suficiente para resolver o Sudoku!\033[0;0m")
            print("\nSolução: \n\n{}".format(sudoku.__str2__()))
            for cel in sudoku.celulas:
                val = sudoku.possibilidades[cel]                
                value.append(val[0])
                
            fim = time.time()
            timeExec = round((fim - inicio), 3)
            print("Tempo de Execução: " + str(timeExec) + " s")
            return str(timeExec)
        else:
            print("\033[33mEste Sudoku não tem resultado com o AC3\033[0;0m")

        
def solve2(grid, index2, total):   # Função para resolver um sudoku aleatório, com a implementação do algoritmo de AC-3
        
    inicio = time.time()
        
    sudoku_aleat = Sudoku(grid)    
    
    print("\n       Sudoku       \n")
    print("{}".format(sudoku_aleat.__str1__(grid)))
        
    print("\nAC3 iniciou")
        
    AC3_result = AC3(sudoku_aleat)
    
    if not AC3_result:
        print("\nEste Sudoku não tem solução")
    
    else:
            
        if sudoku_aleat.terminou():
    
            print("\n\033[32mAC3 é suficiente para resolver o Sudoku!\033[0;0m")
            print("\nSolução: \n\n{}".format(sudoku_aleat.__str2__()))
            for cel in sudoku_aleat.celulas:
                val = sudoku_aleat.possibilidades[cel]                
                value2.append(val[0])
                
            fim = time.time()
            timeExec = round((fim - inicio), 3)
            print("Tempo de Execução: " + str(timeExec) + " s")
            
        else:
            print("\033[33mEste Sudoku não tem resultado com o AC3\033[0;0m")       
    
    def getTimeExec(self):
        return self.timeExec
    
def get_time():            # Função que retorna o tempo de execução, da resolução do sudoku.
    return solve.timeExec

def fetch_sudokus(input):  # Função que verifica se os valores introduzidos nas variáveis “sudoku” e ”sudoku_aleat” estão correctos
    
        DEFAULT_SIZE = 81
    
        if (len(input) % DEFAULT_SIZE) != 0:
            print("Erro: deve ser múltiplo de {}".format(DEFAULT_SIZE))
            sys.exit()
            
        else:
            formatted_input = input.replace("X", "0").replace("#", "0").replace("@", "0")
    
            if not formatted_input.isdigit():
    
                print("Erro: só são permitidos os seguintes caracteres: [1,9], 'X', '#' e '@'")
                sys.exit()
                    
            else:
                return [formatted_input[i:i+DEFAULT_SIZE] for i in range(0, len(formatted_input), DEFAULT_SIZE)]


if __name__ == "__main__":      # Função para executar o solver
    
    sudoku_grid_as_string = sudoku
        
    sudoku_queue = fetch_sudokus(sudoku_grid_as_string)
        
    for index, sudoku_grid in enumerate(sudoku_queue):
        solve(sudoku_grid, index , len(sudoku_queue))
            
    sudoku_grid_as_string2 = sudoku_aleat
    
    sudoku_queue2 = fetch_sudokus(sudoku_grid_as_string2)
        
    for index, sudoku_grid in enumerate(sudoku_queue2):
        solve2(sudoku_grid, index, len(sudoku_queue2))    

