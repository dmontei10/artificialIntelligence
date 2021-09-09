import nltk                         # Bibliotecas de suporte à execução do programa
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string

class Processar_Strings:
    def __init__(self, data, listaStrings):
        self.data = data
        self.listaStrings = listaStrings

    def processamentoPal(self):              # Método para processar as modificações no texto
        for strg in self.data:               
            strg = self.remLetra(strg)       # Aplicação do método remLetra() a strg
            strg = self.convMinusculas(strg) # Aplicação do método convMinusculas() a strg
            strg = self.remPontuacao(strg)   # Aplicação do método remPontuacao() a strg
            strg = self.modDerivadas(strg)   # Aplicação do método modDerivadas() a strg
            strg = self.remStopWords(strg)   # Aplicação do método remStopWords() a strg
            self.listaStrings.append(strg)   # Adicionar o texto processado a listaStrings
            
    def remLetra(self, strg):       # Método para remover as palavras com uma única letra
        texto = strg.split()
        string_alt = ""
        for palavra in texto:
            if(len(palavra) >= 2):
                string_alt += palavra + " "
        return string_alt.strip()
    
    def convMinusculas(self, strg): # Método para converter todas as palavras de cada String letras minúsculas
        string_alt = strg.lower()
        return string_alt
    
    def remPontuacao(self, strg):   # Método para remover todos os caracteres de pontuação
        string_alt = ""
        for char in strg:
            if(char not in string.punctuation):
                string_alt += char
        return string_alt
    
    def modDerivadas(self, strg):   # Método para modificar palavras derivadas como, por exemplo, "Consulting" para "Consult", retirando a parte "ing"
        ps = PorterStemmer()
        texto = strg.split()
        string_alt = ""
        for palavra in texto:
            string_alt += ps.stem(palavra) + " "
        return string_alt

    def remStopWords(self, strg):   # Método para remover as chamadas StopWords, por exemplo: "is", "a" e/ou "the" 
        stopWords = set(stopwords.words('english'))
        string_alt = ""
        for palavra in strg.split():
            if(palavra.lower() not in stopWords):
                string_alt += palavra + " "
        return string_alt.strip()

    def getListaStrings(self):      # Método para retornar os valores da listaStrings
        return self.listaStrings
