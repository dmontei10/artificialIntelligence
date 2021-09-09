from processamento import Processar_Strings # Bibliotecas de suporte à execução do programa
from collections import Counter
import pandas as pd
import numpy as np


class Perceptron:
    def __init__(self):
        self.ficheiro = None                # Inicialização do ficheiro, que recebe o spam.csv
        self.lista_Str = []                 # Inicialização da lista de strings
        self.lista_Pal = []                 # Inicialização da lista de palavras retiradas de lista_Str
        self.freq_Pal = dict()              # Inicialização do dicionário com a frequência de cada palavra em lista_Str
        self.bagOfWords = []                # Inicialização da lista que guarda todas as palavras, sem repetições
        self.lista_Frases = []              # Inicialização da lista de todas as frases
        self.lista_Treino = []              # Inicialização da lista com 70% das frases, para treino
        self.lista_Validacao = []           # Inicialização da lista com 15% das frases, para validacao
        self.lista_Teste = []               # Inicialização da lista com 15% das frases, para teste
        self.tamanho_Treino = 0             # Inicialização da variável tamanho_Treino
        self.tamanho_Validacao = 0          # Inicialização da variável tamanho_Validacao
        self.class_lista_Frases = []        # Inicialização da lista com as classificações da lista_Frases
        self.class_lista_Treino = []        # Inicialização da lista com as classificações da lista_Treino
        self.class_lista_Validacao = []     # Inicialização da lista com as classificações da lista_Validacao
        self.class_lista_Teste = []         # Inicialização da lista com as classificações da lista_Teste
        self.lista_vetores_Treino = []      # Inicialização da lista de vetores de treino
        self.lista_vetores_Validacao = []   # Inicialização da lista de vetores de validacao
        self.lista_vetores_Teste = []       # Inicialização da lista de vetores de teste
        self.lista_vetores_Total = []       # Inicialização da lista de vetores total
        self.peso = []                      # Inicialização da lista de pesos
        self.lista_Previsoes = []           # Inicialização da lista das previsoes
        self.lista_Validacao = []           # Inicialização da lista das previsoes
        self.matriz_Confusao = []           # Inicialização da matriz de confusao
        self.matriz_Relativa = []           # Inicialização da matriz de confusao relativa

    def algoritmo(self):                  # Método que corre os vários passos do algoritmo
        self.processamento()              # Chamada do método processamento()
        self.conv_Texto()                 # Chamada do método conv_Texto()
        self.inic_freq_Pal()              # Chamada do método inic_freq_Pal()
        self.setLista_Frases()            # Chamada do método setLista_Frases()
        self.setLista_Treino()            # Chamada do método setLista_Treino()
        self.setLista_Validacao()         # Chamada do método setLista_Validacao()
        self.setLista_Teste()             # Chamada do método setLista_Teste()
        self.setBagOfWords()              # Chamada do método setBagOfWords()
        self.lista_vetores_Total = self.inic_freq_Vetores(self.lista_Frases)        # Aplicação do método inic_freq_Vetores e atribuição à variável lista_vetores_Total
        self.lista_vetores_Treino = self.inic_freq_Vetores(self.lista_Treino)       # Aplicação do método inic_freq_Vetores e atribuição à variável lista_vetores_Treino
        self.lista_vetores_Validacao = self.inic_freq_Vetores(self.lista_Validacao) # Aplicação do método inic_freq_Vetores e atribuição à variável lista_vetores_Treino
        self.lista_vetores_Teste = self.inic_freq_Vetores(self.lista_Teste)         # Aplicação do método inic_freq_Vetores e atribuição à variável lista_vetores_Teste
        self.setClass_lista_Frases()      # Chamada do método setClass_lista_Frases()
        self.setClass_lista_Treino()      # Chamada do método setClass_lista_Treino()
        self.setClass_lista_Validacao()   # Chamada do método setClass_lista_Validacao()
        self.setClass_lista_Teste()       # Chamada do método setClass_lista_Teste()
        self.setPeso()                    # Chamada do método setPeso()           
        self.conv_Pesos()                 # Chamada do método conv_Pesos()           
        #self.def_ResultadosVal()          # Chamada do método def_ResultadosVal()
        self.def_ResultadosTes()          # Chamada do método def_ResultadosVal()
        self.getMetricas()                # Chamada do método getMetricas()

    def processamento(self):              # Método para ler o ficheiro e processar o texto
        self.ficheiro = pd.read_csv("spam.csv", encoding = "latin-1")
        self.ficheiro = self.ficheiro.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis = 1)
        self.ficheiro = self.ficheiro.rename(columns = {"v1": "Tipo", "v2": "Texto"})
        
        proc_palavra = Processar_Strings(self.ficheiro["Texto"], self.lista_Str)
        proc_palavra.processamentoPal()

    def conv_Texto(self):                 # Método para converter as frases de lista_Str em palavras individuais
        for texto in self.lista_Str: 
            self.lista_Pal.extend(texto.split())
        self.lista_Pal.sort()

    def inic_freq_Pal(self):              # Método para contar e adicionar a um dicionário a lista de palavras lista_Pal
        self.freq_Pal = dict(Counter(self.lista_Pal)) 
        self.freq_Pal = dict(sorted(self.freq_Pal.items(), key = lambda kv:(kv[1], kv[0]), reverse = True))
    
    def setLista_Frases(self):         # Método para inserir todas as frases na lista_Frases
        for linha in self.lista_Str:
            self.lista_Frases.append(linha)
        
    def setLista_Treino(self):         # Método que define o conjunto de treino, 70%
        self.tamanho_Treino = round(len(self.lista_Frases) * 0.7)
        self.tamanho_Validacao = round(len(self.lista_Frases) * (1 - 0.15))
        self.lista_Treino = self.lista_Frases[:self.tamanho_Treino]
        
    def setLista_Validacao(self):      # Método que define o conjunto de validacao, 15%
        self.lista_Validacao = self.lista_Frases[self.tamanho_Treino:self.tamanho_Validacao]

    def setLista_Teste(self):          # Método que define o conjunto de teste, 15%
        self.lista_Teste = self.lista_Frases[self.tamanho_Validacao:] 
    
    def setBagOfWords(self):           # Método para inserir valores na bag of words da lista de treino
        palavras = []
        for texto in self.lista_Treino: 
            palavras.extend(texto.split()) 

        for palavra in palavras:
            if(palavra not in self.bagOfWords):
                self.bagOfWords.append(palavra)

        self.bagOfWords.sort() 
    
    def inic_freq_Vetores(self, lista):   # Método para criar vetores de frequencia para cada frase do conjunto de dados respectivo
        vetores = []
        for texto in lista:
            palavras = texto.split()
            vetor = []
            for palavra in self.bagOfWords:
                if(palavra in palavras):
                    vetor.append(palavras.count(palavra))
                else:
                    vetor.append(0) 
            vetores.append(vetor)

        return vetores
        
    def setClass_lista_Frases(self):      # Método que adiciona 1 ou -1 à classificação da lista de frases, se o tipo for "ham" ou "spam", respectivamente
        for tipo in self.ficheiro["Tipo"]:
            if(tipo == 'ham'):
                self.class_lista_Frases.append(1)
            else:
                self.class_lista_Frases.append(-1)
    
    def setClass_lista_Treino(self):   # Método para definir a classificação da lista de treino, com base no tamanho do treino, 70%
        self.class_lista_Treino = self.class_lista_Frases[:self.tamanho_Treino]
    
    def setClass_lista_Validacao(self):    # Método para definir a classificação da lista de teste, com base no resto do tamanho do treino, 30%
        self.class_lista_Validacao = self.class_lista_Frases[self.tamanho_Treino:self.tamanho_Validacao]
        
    def setClass_lista_Teste(self):    # Método para definir a classificação da lista de teste, com base no resto do tamanho do treino, 30%
        self.class_lista_Teste = self.class_lista_Frases[self.tamanho_Validacao:]

    def setPeso(self):                 # Método para definir o peso
        self.peso = [0]*len(self.bagOfWords)
    
    def conv_Pesos(self):                  # Método que atualiza os pesos
        self.t = 3                                                                                  
        for i in range(self.t):
            pos = 0                                                                                  
            for vetor in self.lista_vetores_Treino:                  
                for k in range(len(self.bagOfWords)):                                                
                    mult = self.peso[k] * vetor[k]
                if(self.class_lista_Treino[pos] * mult <= 0):                                        
                    for l in range(len(self.bagOfWords)):                                            
                        self.peso[l] = self.peso[l] + self.class_lista_Treino[pos] * vetor[l]        
                pos += 1
    
    def def_ResultadosVal(self):        # Método que determina se a frase é Spam ou Ham, com base nos valores para validacao
        for vetor in self.lista_vetores_Validacao: 
            resultado = 0
            for i in range(len(self.bagOfWords)): 
                resultado += self.peso[i] * vetor[i]

            x = np.sign(resultado)

            if(x == -1):        
                self.lista_Validacao.append(-1)
            else:
                self.lista_Validacao.append(1)
                
    def def_ResultadosTes(self):        # Método que determina se a frase é Spam ou Ham, com base nos valores para teste
        for vetor in self.lista_vetores_Teste: 
            resultado = 0
            for i in range(len(self.bagOfWords)): 
                resultado += self.peso[i] * vetor[i]

            x = np.sign(resultado)

            if(x == -1):        
                self.lista_Previsoes.append(-1)
            else:
                self.lista_Previsoes.append(1)

    def getMetricas(self):             # Método para obter as métricas do classificador e obter os seus resultados
        labels = [1, 0]
        if(len(self.class_lista_Teste) != len(self.lista_Previsoes)):
            return None

        verdadeiro = labels[0]
        falso = labels[1]

        verdadeiros_Positivos = 0      
        verdadeiros_Negativos = 0       

        falsos_Positivos = 0      
        falsos_Negativos = 0      

        for (i, valor) in enumerate(self.class_lista_Teste):
            previsao = self.lista_Previsoes [i]

            if valor == verdadeiro:
                verdadeiros_Positivos += 1 if previsao == valor else 0
                falsos_Positivos += 1 if previsao != valor else 0 
            else:
                verdadeiros_Negativos += 1 if previsao == valor else 0
                falsos_Negativos += 1 if previsao != valor else 0
        
        
        self.exatidao = ((verdadeiros_Positivos + verdadeiros_Negativos) / 
                         (verdadeiros_Positivos + falsos_Positivos + 
                          verdadeiros_Negativos + falsos_Negativos)) * 100
        
        self.sensibilidade = (verdadeiros_Positivos / (verdadeiros_Positivos + falsos_Negativos)) * 100
        
        self.precisao = (verdadeiros_Positivos / (verdadeiros_Positivos 
                                                    + falsos_Positivos)) * 100
        
        self.fScore = 2 * (float(self.sensibilidade * self.precisao) /
                           float(self.sensibilidade + self.precisao))
        
        self.matriz_Confusao = np.array([[verdadeiros_Positivos, falsos_Positivos],
                                         [falsos_Negativos, verdadeiros_Negativos]])
        
        self.matriz_Relativa = np.array([[round(verdadeiros_Positivos/(verdadeiros_Positivos + falsos_Positivos), 3), 
                                          round(falsos_Negativos/(verdadeiros_Negativos + falsos_Negativos), 3)], 
                                         [round(falsos_Positivos/(verdadeiros_Positivos + falsos_Positivos), 3), 
                                          round(verdadeiros_Negativos/(verdadeiros_Negativos + falsos_Negativos), 3)]])
        
        print("\n-------------- Perceptron -------------\n")
        print("------ Métricas de Classificação ------\n")
        print("Exatidão {:0.3f}" .format(self.exatidao))
        print("Sensibilidade {:0.3f}" .format(self.sensibilidade))
        print("Precisão {:0.3f}" .format(self.precisao))
        print("fScore {:0.3f}\n" .format(self.fScore))
        
        print("---------- Matriz de Confusão ---------\n")
        print(self.matriz_Confusao)
        print()
        print(self.matriz_Relativa)