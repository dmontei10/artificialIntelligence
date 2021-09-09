from processamento import Processar_Strings # Bibliotecas de suporte à execução do programa
import pandas as pd
import numpy as np
import math
import random

class NaiveBayes:
    def __init__(self):
        self.ficheiro = None            # Inicialização da variável ficheiro, que contém os dados lidos de "spam.csv"
        self.lista = []                 # Inicialização da lista com o texto, após ser processado
        self.x_treino = []              # Inicialização da lista com o conjunto de treino de x
        self.y_treino = []              # Inicialização da lista com o conjunto de treino de y
        self.x_teste = []               # Inicialização da lista com o conjunto de teste de x
        self.y_teste = []               # Inicialização da lista com o conjunto de teste de y
        self.x_validacao = []           # Inicialização da lista com o conjunto de validação de x
        self.y_validacao = []           # Inicialização da lista com o conjunto de validação de y
        self.spam = 0                   # Inicialização da variável spam
        self.ham = 0                    # Inicialização da variável ham
        self.totalPalavras = []         # Inicialização da lista com o conjunto total de palavras
        self.matrizP = {}               # Inicialização da matriz P
        self.matrizP_Relativa = {}      # Inicialização da matriz P relativa
        self.b = 0                      # Inicialização da variável b
        self.c = 158698421              # Inicialização da variável c
        self.confMatriz = None          # Inicialização da matriz de confusão
        self.confMatriz_Relativa = None # Inicialização da matriz de confusão relativa

    def algoritmo(self):                                                 # Método que corre os vários passos do algoritmo
        self.processamento()                                             # Chamada do método processamento()
        self.train_X_Y()                                                 # Chamada do método train_X_Y()
        self.lista_Palavras(self.getX_treino())                          # Chamada do método lista_Palavras()
        self.computacao_Ham_Spam(self.getX_treino(), self.getY_treino()) # Chamada do método computacao_Ham_Spam()
        self.inicializa_P()                                              # Chamada do método inicializa_P()
        self.contar_Palavras()                                           # Chamada do método contar_Palavras()
        self.normalizar_Contagem()                                       # Chamada do método normalizar_Contagem()
        self.inicializa_B()                                              # Chamada do método inicializa_B()
        self.classificar(self.getX_treino(), self.getY_treino())         # Chamada do método classificar()
        
    def processamento(self):            # Método para ler o ficheiro e processar o texto
        self.ficheiro = pd.read_csv("spam.csv", encoding = "latin-1")
        self.ficheiro = self.ficheiro.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis = 1)
        self.ficheiro = self.ficheiro.rename(columns = {"v1": "Tipo", "v2": "Texto"})
            
        proc_palavra = Processar_Strings(self.ficheiro["Texto"], self.lista)
        proc_palavra.processamentoPal()
    
    def train_X_Y(self):                # Método para definir o conjunto de treino, teste e validação    
        y = self.ficheiro["Tipo"]
        y = np.array(y)
            
        validacao_Inverso = round(len(self.lista) * 0.7)
        teste_Inverso = round(len(self.lista) * 0.85)
            
        self.x_treino, self.y_treino,  = self.lista[:validacao_Inverso], y[:validacao_Inverso]
        
        self.x_validacao, self.y_validacao = self.lista[validacao_Inverso:teste_Inverso], y[validacao_Inverso:teste_Inverso]
        
        self.x_teste, self.y_teste = self.lista[teste_Inverso:], y[teste_Inverso:]
   
    def lista_Palavras(self, x_treino): # Método para criar uma lista de todas as palavras contidas no conjunto de treino
        for email in x_treino:
            for palavra in email.split():
                if palavra not in self.totalPalavras:
                    self.totalPalavras.append(palavra)
                    
    def computacao_Ham_Spam(self, X_treino, Y_treino): # Método para calcular o número de mensagens spam e ham
        x_treino = np.array(X_treino)
        y_treino = np.array(Y_treino)

        total = 0
        
        for tipo in y_treino:
            if(tipo == "spam"):
                self.spam += 1
            else:
                self.ham += 1
            total += 1
        
        print("\n------------- Naïve Bayes -------------")
        print("\nNúmero de mensagens de treino Spam: ", self.spam)
        print("Número de mensagens de treino Ham: ", self.ham)
        print("Número Total de mensagens de treino: ", total)
    
    def inicializa_B(self): # Método para calcular o valor da variável b
        self.b = math.log(self.c) + math.log(self.ham) - math.log(self.spam)
               
    def inicializa_P(self): # Método para criar uma matriz P com todas as palavras do totalPalavras
       for palavra in self.totalPalavras:
           self.matrizP[palavra] = [1, 1]
        
    def contar_Palavras(self): # Método para contar quantas determinada palavra surge em sms/email spam ou sms/email ham
        X_treino = np.array(self.x_treino)
        Y_treino = np.array(self.y_treino)
        
        for i in range(len(X_treino)):
            if Y_treino[i] == "spam":
                for palavra in self.totalPalavras:
                    if palavra in X_treino[i]:
                        self.matrizP[palavra][0] += 1
            else:
                for palavra in self.totalPalavras:
                    if palavra in X_treino[i]:
                        self.matrizP[palavra][1] += 1
                  
    def normalizar_Contagem(self): # Método para converter os valores absolutos da Matriz P em valores relativos, numa nova matriz
        palavras_totais_spam = 0
        palavras_totais_ham = 0
        self.matrizP_Relativa = dict()

        for x in self.matrizP:
            palavras_totais_spam += self.matrizP[x][0]
            palavras_totais_ham += self.matrizP[x][1]
            self.matrizP_Relativa[x] = [self.matrizP[x][0], self.matrizP[x][1]]

        for x in self.matrizP_Relativa:
            self.matrizP_Relativa[x][0] = self.matrizP_Relativa[x][0] / palavras_totais_spam
            self.matrizP_Relativa[x][1] = self.matrizP_Relativa[x][1] / palavras_totais_ham

        self.palavras_totais_spam = palavras_totais_spam
        self.palavras_totais_ham = palavras_totais_ham

    def classificar(self, x, y): # Método para classificar o sms/email como spam ou ham e obter o valor das métricas
        x_treino = np.array(x)
        y_treino = np.array(y)

        verdadeiros_Positivos = 0
        falsos_Negativos = 0
        verdadeiros_Negativos = 0
        falsos_Positivos = 0
        
        for i in range(len(x_treino)):
            t = self.limite_T(x_treino[i])

            if t > 0 and y_treino[i] == "spam":
                verdadeiros_Positivos += 1
            if t > 0 and y_treino[i] == "ham":
                falsos_Negativos += 1
            if t < 0 and y_treino[i] == "ham":
                verdadeiros_Negativos += 1
            if t < 0 and y_treino[i] == "spam":
                falsos_Positivos += 1
                t = self.limite_T(x_treino[i])
        
        self.exatidao = ((verdadeiros_Positivos + verdadeiros_Negativos) /
                         (verdadeiros_Positivos + verdadeiros_Negativos + 
                          falsos_Positivos + falsos_Negativos)) * 100
        
        self.sensibilidade = (verdadeiros_Positivos / (verdadeiros_Positivos + falsos_Negativos)) * 100
             
        self.precisao = (verdadeiros_Positivos / (verdadeiros_Positivos 
                                                    + falsos_Positivos)) * 100
        
        self.fScore = 2 * (float(self.sensibilidade * self.precisao) /
                           float(self.sensibilidade + self.precisao))
        
        self.confMatriz = np.array([[verdadeiros_Positivos, falsos_Negativos], [falsos_Positivos, verdadeiros_Negativos]])
        
        self.confMatriz_Relativa = np.array([[round(verdadeiros_Positivos/(verdadeiros_Positivos + falsos_Positivos), 3), 
                                              round(falsos_Negativos/(verdadeiros_Negativos + falsos_Negativos), 3)], 
                                             [round(falsos_Positivos/(verdadeiros_Positivos + falsos_Positivos), 3), 
                                              round(verdadeiros_Negativos/(verdadeiros_Negativos + falsos_Negativos), 3)]])
        
        print("\n------ Métricas de Classificação ------\n")
        print("Exatidão {:0.3f}" .format(self.exatidao))
        print("Sensibilidade {:0.3f}" .format(self.sensibilidade))
        print("Precisão {:0.3f}" .format(self.precisao))
        print("fScore {:0.3f}\n" .format(self.fScore))
        
        print("---------- Matriz de Confusão ---------\n")
        print(self.confMatriz)
        print()
        print(self.confMatriz_Relativa)
        
    def limite_T(self, email): # Método para calcular t
        t = self.b * (-1)
        vetor = []
        vetorAux = []

        for word in email.split():
            vetor.append(word)
            for ele in vetor:
                if ele in vetorAux:
                    pass
                else:
                    if str(ele) in self.matrizP_Relativa:
                        t += vetor.count(ele) * (math.log(self.matrizP_Relativa[ele][0] - math.log(self.matrizP_Relativa[ele][1])))
                        vetorAux.append(ele)
                    else:
                        pass

        return t
    
    def obterLogC(self):       # Método para calcular o valor de C 
       
        self.computacao_Ham_Spam(self.x_treino, self.y_treino)
        self.lista_Palavras(self.x_treino)
        self.inicializa_P()
        self.contar_Palavras()
        self.normalizar_Contagem()
        previ = 90
        i = 1

        vetor = list(range(100000000, 1000000000, 1))
        random.shuffle(vetor)

        while self.precisao <= 90:
            if previ < 90:
                vetor.remove(vetor[0])

            previ = self.precisao
            print("Valor de C: ", self.c)
            print("processo: ", i)
            self.inicializa_B()
            self.classificar(self.x_validacao, self.y_validacao)
            print(previ)
            i += 1
            self.c = vetor[0]
            
    def getX_treino(self): # Método para retornar o valor de x_treino
        return self.x_treino

    def getY_treino(self): # Método para retornar o valor de y_treino
        return self.y_treino