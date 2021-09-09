from tkinter import *                          # Bibliotecas de suporte à execução do programa
from tkinter import messagebox
import sys
from naiveBayes import NaiveBayes
from perceptrao import Perceptron

class GUI_Spam():                              # Classe que origina a interface para os filtros de Spam
    def __init__(self):                        # Janela Inicial
        
        self.window = Tk()
        variavel_controlo = BooleanVar(self.window)
            
        nb=NaiveBayes()    
            
        self.window.title('Filtro de Spam')
        self.window.resizable(False, False)
        self.window.geometry('600x450+584+230')
            
        labelwel = Label(self.window)
        labelwel.place(relx=0.125, rely=0.325, height=75, width=450)
        labelwel.configure(background="#0082ba", foreground="white", relief='ridge', text='''Classificadores Filtro Spam''', font=("Rockwell", 14))
            
        def menuNaiveBayes():                  # janela do filtro de spam Naive Bayes
            self.window2 = Tk()
            variavel_controlo = BooleanVar(self.window2)
            
            nb=NaiveBayes()    
            
            self.window2.title('Naïve Bayes')
            self.window2.resizable(False, False)
            self.window2.geometry('600x450+584+230')
            self.window2.configure(background="#91cded")
            
            labelwel = Label(self.window2)
            labelwel.place(relx=0.25, rely=0.067, height=35, width=305)
            labelwel.configure(background="#0082ba", foreground="white", relief='ridge', text='''Classificador Naïve Bayes''', font=("Rockwell", 14))
            
            frame1 = Frame(self.window2)
            frame1.place(relx=0.125, rely=0.225, relheight=0.250, relwidth=0.750)
            frame1.configure(relief='groove', borderwidth="2", width=305)
            labelframe = LabelFrame(frame1, text="Opções")
            labelframe.pack(fill="both", expand="yes")
            labelframe.configure(background="#f7f7f7")
                
            frame2 = Frame(self.window2)
            frame2.place(relx=0.125, rely=0.500, relheight=0.475, relwidth=0.350)
            frame2.configure(relief='groove', borderwidth="2", width=305)
            labelframe2 = LabelFrame(frame2, text="Métricas")
            labelframe2.pack(fill="both", expand="yes")
                
            frame3 = Frame(self.window2)
            frame3.place(relx=0.525, rely=0.500, relheight=0.475, relwidth=0.350)
            frame3.configure(relief='groove', borderwidth="2", width=305)
            labelframe3 = LabelFrame(frame3, text="Palavras e Matrizes")
            labelframe3.pack(fill="both", expand="yes")
            
            def menuLista():                   # Janela de frequência de palavras absolutas e relativas do Naive Bayes
                if variavel_controlo.get() == False:
                    messagebox.showerror(title="Erro", message="Inicie o Classificador Naïve Bayes.")
                else:
                    
                    palavras = nb.matrizP
                    palavrasRel = nb.matrizP_Relativa
                    
                    window9 = Toplevel()
                    window9.resizable(False, False)
                    window9.title('Frequências de Palavras')
                    window9.geometry("700x450+517+216")
                    
                    frame1 = Frame(window9)
                    frame1.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=0.508)
                    frame1.configure(relief='raised', borderwidth="2", width=700, background="#91cded")
                    
                    titleA = Label(frame1)
                    titleA.place(relx=0.325, rely=0.0, height=40, width=125)
                    titleA.configure(relief="ridge", text="""Absolutas""", fg='white', background="#028f99", font=("Rockwell", 10))
                    
                    labeltitle = Label(frame1)
                    labeltitle.place(relx=0.035, rely=0.138, height=31, width=80)
                    labeltitle.configure(relief="ridge", text="""Palavra:""", fg='white', background="#0082ba", font=("Rockwell", 9))
                    
                    labeltitle2 = Label(frame1)
                    labeltitle2.place(relx=0.625, rely=0.138, height=31, width=50)
                    labeltitle2.configure(relief="ridge", text="""Spam""", fg='white', background="#0082ba", font=("Rockwell", 9))
                    
                    labeltitle3 = Label(frame1)
                    labeltitle3.place(relx=0.805, rely=0.138, height=31, width=50)
                    labeltitle3.configure(relief="ridge", text="""Ham""", fg='white', background="#0082ba", font=("Rockwell", 9))
                    
                    palAbs = Text(frame1)
                    
                    for i, j in palavras.items():
                        lista = "{:22s}".format(str(i)) + "{:3s}".format(str(j[0])) + "   " + "{:3s}".format(str(j[1])) + "\n"
                        palAbs.insert(END, lista)
                        
                    palAbs.place(relx=0.035, rely=0.225, relheight=0.700, relwidth=0.915)
                    palAbs.configure(width=174, state='disabled')
                    
                    frame2 = Frame(window9)
                    frame2.place(relx=0.5, rely=0.0, relheight=1.011, relwidth=0.508)
                    frame2.configure(relief='raised', borderwidth="2", width=700, background="#91cded")
                    
                    title = Label(frame2)
                    title.place(relx=0.325, rely=0.0, height=40, width=125)
                    title.configure(relief="ridge", text="""Relativas""", fg='white', background="#028f99", font=("Rockwell", 10))
                    
                    labeltitle2 = Label(frame2)
                    labeltitle2.place(relx=0.035, rely=0.138, height=31, width=80)
                    labeltitle2.configure(relief="ridge", text="""Palavra:""", fg='white', background="#0082ba", font=("Rockwell", 9))
                    
                    labeltitle2_2 = Label(frame2)
                    labeltitle2_2.place(relx=0.565, rely=0.138, height=31, width=50)
                    labeltitle2_2.configure(relief="ridge", text="""Spam""", fg='white', background="#0082ba", font=("Rockwell", 9))
                    
                    labeltitle3_2 = Label(frame2)
                    labeltitle3_2.place(relx=0.765, rely=0.138, height=31, width=50)
                    labeltitle3_2.configure(relief="ridge", text="""Ham""", fg='white', background="#0082ba", font=("Rockwell", 9))
                    
                    palRel = Text(frame2)
                    
                    for i, j in palavrasRel.items():
                        lista = "{:18s}".format(str(i)) + "{:0.4f}".format(j[0]) + " " + "{:0.4f}".format(j[1]) + "\n"
                        palRel.insert(END, lista)
                        
                    palRel.place(relx=0.035, rely=0.225, relheight=0.700, relwidth=0.915)
                    palRel.configure(width=174, state='disabled')
                    
                    window9.mainloop()
                
            def iniciar():                  # Funcao para iniciar o algoritmo de Naive Bayes
                variavel_controlo.set(True)        
                nb.algoritmo()        
        
            def exatidao():                 # Funcao para retornar o valor da exatidao de Naive Bayes
                if variavel_controlo.get() == True:
                    messagebox.showinfo(title="Exatidão", message='''{:0.3f} %'''.format(nb.exatidao))
                else:
                    messagebox.showerror(title="Erro", message="Inicie o Classificador Naïve Bayes.")
            
            def sensibilidade():            # Funcao para retornar o valor da sensibilidade de Naive Bayes
                if variavel_controlo.get() == True:
                    messagebox.showinfo(title="Sensibilidade", message='''{:0.3f} %''' .format(nb.sensibilidade))
                else:
                    messagebox.showerror(title="Erro", message="Inicie o Classificador Naïve Bayes.")
        
            def precisao():                 # Funcao para retornar o valor da precisao de Naive Bayes
                if variavel_controlo.get() == True:
                    messagebox.showinfo(title="Precisão", message='''{:0.3f} %''' .format(nb.precisao))
                else:
                    messagebox.showerror(title="Erro", message="Inicie o Classificador Naïve Bayes.")
        
            def fScore():                   # Funcao para retornar o valor de fScore de Naive Bayes
                if variavel_controlo.get() == True:
                    messagebox.showinfo(title="fScore", message='''{:0.3f} %''' .format(nb.fScore))
                else:
                    messagebox.showerror(title="Erro", message="Inicie o Classificador Naïve Bayes.")
        
            def MatrizC():                  # Funcao para retornar a matriz de confusao de Naive Bayes
                if variavel_controlo.get() == True:
                    messagebox.showinfo(title="Matriz de Confusão", message=str(nb.confMatriz))
                else:
                    messagebox.showerror(title="Erro", message="Inicie o Classificador Naïve Bayes.")
        
            def MatrizRel():                # Funcao para retornar a matriz de confusao relativa de Naive Bayes
                if variavel_controlo.get() == True:
                    messagebox.showinfo(title="Matriz Conf. Relativa", message=str(nb.confMatriz_Relativa))
                else:
                    messagebox.showerror(title="Erro", message="Inicie o Classificador Naïve Bayes.")
            
            buttonlista = Button(frame1, command=lambda: iniciar())
            buttonlista.place(relx=0.075, rely=0.400, height=35, width=150)
            buttonlista.configure(text='''Iniciar''', pady="0", width=267, background="#9ef702", foreground="black", font=("Rockwell", 11))
                
            buttonclose = Button(frame1, command=self.window2.destroy)
            buttonclose.place(relx=0.475, rely=0.400, height=35, width=200)
            buttonclose.configure(text='''Fechar Classificador''', pady="0", width=267, background="#f74702", foreground="white", font=("Rockwell", 11))
            
            buttonExat = Button(frame2, command=lambda: exatidao())
            buttonExat.place(relx=0.135, rely=0.150, height=30, width=150)
            buttonExat.configure(text='''Exatidão''', pady="0", width=267, background="#028f99", foreground="white", font=("Rockwell", 10))
                
            buttonSensibilidade = Button(frame2, command=lambda: sensibilidade())
            buttonSensibilidade.place(relx=0.135, rely=0.375, height=30, width=150)
            buttonSensibilidade.configure(text='''Sensibilidade''', pady="0", width=267, background="#028f99", foreground="white", font=("Rockwell", 10))
                
            buttonPrecisao = Button(frame2, command=lambda: precisao())
            buttonPrecisao.place(relx=0.135, rely=0.600, height=30, width=150)
            buttonPrecisao.configure(text='''Precisão''', pady="0", width=267, background="#028f99", foreground="white", font=("Rockwell", 10))
                
            buttonfScore = Button(frame2, command=lambda: fScore())
            buttonfScore.place(relx=0.135, rely=0.825, height=30, width=150)
            buttonfScore.configure(text='''fScore''', pady="0", width=267, background="#028f99", foreground="white", font=("Rockwell", 10))
                
            buttonLista = Button(frame3, command=lambda: menuLista())
            buttonLista.place(relx=0.075, rely=0.225, height=30, width=175)
            buttonLista.configure(text='''Frequência Palavras''', pady="0", width=267, background="#028f99", foreground="white", font=("Rockwell", 10))
                
            buttonMatrizC = Button(frame3, command=lambda: MatrizC())
            buttonMatrizC.place(relx=0.075, rely=0.475, height=30, width=175)
            buttonMatrizC.configure(text='''Matriz de Confusão''', pady="0", width=267, background="#028f99", foreground="white", font=("Rockwell", 10))
                
            buttonMatrizRel = Button(frame3, command=lambda: MatrizRel())
            buttonMatrizRel.place(relx=0.075, rely=0.725, height=30, width=175)
            buttonMatrizRel.configure(text='''Matriz Conf. Relativa''', pady="0", width=267, background="#028f99", foreground="white", font=("Rockwell", 10))
                
        def menuPerceptron():               # Janela do filtro de spam Perceptrao
            self.window3 = Tk()
            variavel_controlo = BooleanVar(self.window3)
            
            pt = Perceptron()    
            
            self.window3.title('Perceptron')
            self.window3.resizable(False, False)
            self.window3.geometry('600x475+584+230')
            self.window3.configure(background="#91cded")
            
            labelwel = Label(self.window3)
            labelwel.place(relx=0.25, rely=0.067, height=35, width=305)
            labelwel.configure(background="#0082ba", foreground="white", relief='ridge', text='''Classificador Perceptron''', font=("Rockwell", 14))
            
            frame1 = Frame(self.window3)
            frame1.place(relx=0.125, rely=0.225, relheight=0.250, relwidth=0.750)
            frame1.configure(relief='groove', borderwidth="2", width=305)
            labelframe = LabelFrame(frame1, text="Opções")
            labelframe.pack(fill="both", expand="yes")
            labelframe.configure(background="#f7f7f7")
                
            frame2 = Frame(self.window3)
            frame2.place(relx=0.125, rely=0.500, relheight=0.475, relwidth=0.350)
            frame2.configure(relief='groove', borderwidth="2", width=305)
            labelframe2 = LabelFrame(frame2, text="Métricas")
            labelframe2.pack(fill="both", expand="yes")
                
            frame3 = Frame(self.window3)
            frame3.place(relx=0.525, rely=0.500, relheight=0.475, relwidth=0.350)
            frame3.configure(relief='groove', borderwidth="2", width=305)
            labelframe3 = LabelFrame(frame3, text="Palavras e Matrizes")
            labelframe3.pack(fill="both", expand="yes")
            
            def menuListaPerc():            # Janela da quantidade de palavras do Perceptron
                if variavel_controlo.get() == False:
                    messagebox.showerror(title="Erro", message="Inicie o Classificador Perceptron.")
                else:
                    
                    palavras = pt.freq_Pal
                    
                    window10 = Toplevel()
                    window10.resizable(False, False)
                    window10.title('Frequências de Palavras')
                    window10.geometry("350x450+517+216")
                    
                    frame1 = Frame(window10)
                    frame1.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
                    frame1.configure(relief='raised', borderwidth="2", width=700, background="#91cded")
                    
                    titleA = Label(frame1)
                    titleA.place(relx=0.325, rely=0.0, height=40, width=125)
                    titleA.configure(relief="ridge", text="""Frequência""", fg='white', background="#028f99", font=("Rockwell", 10))
                    
                    labeltitle = Label(frame1)
                    labeltitle.place(relx=0.035, rely=0.138, height=31, width=80)
                    labeltitle.configure(relief="ridge", text="""Palavra:""", fg='white', background="#0082ba", font=("Rockwell", 9))
                    
                    labeltitle2 = Label(frame1)
                    labeltitle2.place(relx=0.665, rely=0.138, height=31, width=100)
                    labeltitle2.configure(relief="ridge", text="""Quantidade""", fg='white', background="#0082ba", font=("Rockwell", 9))
                    
                    palAbs = Text(frame1)
                    
                    for chave, valor in palavras.items():
                        lista = "{:26s}".format(str(chave)) + "{:3s}\n".format(str(valor))
                        palAbs.insert(END, lista)
                        
                    palAbs.place(relx=0.035, rely=0.225, relheight=0.700, relwidth=0.915)
                    palAbs.configure(width=174, state='disabled')
                    
                    window10.mainloop()
                
            def iniciar():              # Funcao para iniciar o algoritmo de Perceptron
                variavel_controlo.set(True)        
                pt.algoritmo()        
        
            def exatidao():             # Funcao para retornar o valor da exatidao de Perceptron
                if variavel_controlo.get() == True:
                    messagebox.showinfo(title="Exatidão", message='''{:0.3f} %'''.format(pt.exatidao))
                else:
                    messagebox.showerror(title="Erro", message="Inicie o Classificador Perceptron.")
            
            def sensibilidade():        # Funcao para retornar o valor da sensibilidade de Perceptron
                if variavel_controlo.get() == True:
                    messagebox.showinfo(title="Sensibilidade", message='''{:0.3f} %''' .format(pt.sensibilidade))
                else:
                    messagebox.showerror(title="Erro", message="Inicie o Classificador Perceptron.")
        
            def precisao():             # Funcao para retornar o valor da precisao de Perceptron
                if variavel_controlo.get() == True:
                    messagebox.showinfo(title="Precisão", message='''{:0.3f} %''' .format(pt.precisao))
                else:
                    messagebox.showerror(title="Erro", message="Inicie o Classificador Perceptron.")
        
            def fScore():               # Funcao para retornar o valor de fscore de Perceptron
                if variavel_controlo.get() == True:
                    messagebox.showinfo(title="fScore", message='''{:0.3f} %''' .format(pt.fScore))
                else:
                    messagebox.showerror(title="Erro", message="Inicie o Classificador Perceptron.")
        
            def MatrizC():              # Funcao para retornar o valor da matriz de confusao de Perceptron
                if variavel_controlo.get() == True:
                    messagebox.showinfo(title="Matriz de Confusão", message=str(pt.matriz_Confusao))
                else:
                    messagebox.showerror(title="Erro", message="Inicie o Classificador Perceptron.")
        
            def MatrizRel():            # Funcao para retornar o valor da matriz de confusao relativa de Perceptron
                if variavel_controlo.get() == True:
                    messagebox.showinfo(title="Matriz Conf. Relativa", message=str(pt.matriz_Relativa))
                else:
                    messagebox.showerror(title="Erro", message="Inicie o Classificador Perceptron.")
            
            buttonlista = Button(frame1, command=lambda: iniciar())
            buttonlista.place(relx=0.075, rely=0.400, height=35, width=150)
            buttonlista.configure(text='''Iniciar''', pady="0", width=267, background="#9ef702", foreground="black", font=("Rockwell", 11))
                
            buttonclose = Button(frame1, command=self.window3.destroy)
            buttonclose.place(relx=0.475, rely=0.400, height=35, width=200)
            buttonclose.configure(text='''Fechar Classificador''', pady="0", width=267, background="#f74702", foreground="white", font=("Rockwell", 11))
            
            buttonExat = Button(frame2, command=lambda: exatidao())
            buttonExat.place(relx=0.135, rely=0.150, height=30, width=150)
            buttonExat.configure(text='''Exatidão''', pady="0", width=267, background="#028f99", foreground="white", font=("Rockwell", 10))
                
            buttonSensibilidade = Button(frame2, command=lambda: sensibilidade())
            buttonSensibilidade.place(relx=0.135, rely=0.375, height=30, width=150)
            buttonSensibilidade.configure(text='''Sensibilidade''', pady="0", width=267, background="#028f99", foreground="white", font=("Rockwell", 10))
                
            buttonPrecisao = Button(frame2, command=lambda: precisao())
            buttonPrecisao.place(relx=0.135, rely=0.600, height=30, width=150)
            buttonPrecisao.configure(text='''Precisão''', pady="0", width=267, background="#028f99", foreground="white", font=("Rockwell", 10))
                
            buttonfScore = Button(frame2, command=lambda: fScore())
            buttonfScore.place(relx=0.135, rely=0.825, height=30, width=150)
            buttonfScore.configure(text='''fScore''', pady="0", width=267, background="#028f99", foreground="white", font=("Rockwell", 10))
                
            buttonLista = Button(frame3, command=lambda: menuListaPerc())
            buttonLista.place(relx=0.075, rely=0.225, height=30, width=175)
            buttonLista.configure(text='''Frequência Palavras''', pady="0", width=267, background="#028f99", foreground="white", font=("Rockwell", 10))
                
            buttonMatrizC = Button(frame3, command=lambda: MatrizC())
            buttonMatrizC.place(relx=0.075, rely=0.475, height=30, width=175)
            buttonMatrizC.configure(text='''Matriz de Confusão''', pady="0", width=267, background="#028f99", foreground="white", font=("Rockwell", 10))
                
            buttonMatrizRel = Button(frame3, command=lambda: MatrizRel())
            buttonMatrizRel.place(relx=0.075, rely=0.725, height=30, width=175)
            buttonMatrizRel.configure(text='''Matriz Conf. Relativa''', pady="0", width=267, background="#028f99", foreground="white", font=("Rockwell", 10))
        
        def creditos():                     # Funcao para mostrar os creditos do trabalho
                        messagebox.showinfo('Créditos',"""  
                        Elaborado por:                         
                                                                
                         - {:20s}       -   Nº 30003769       
                         - {:20s}   -   Nº 30003043       
                         - {:20s}    -   Nº 30005711       
                         - {:20s}    -   Nº 30003039       
                                                                
                                Inteligência Artificial        
                         @UAL - Universidade Autónoma de Lisboa     
                        """.format('Bruno Silva', 'David Monteiro', 'Nuno Barrocas', 'Zacarias Chiena'))
        
        def quit_program():             # Funcao para Sair do programa
            self.window.quit()
            self.window.destroy()
        
        def on_closing():               # Funcao para terminar/fechar a janela do programa de filtro de spam
            if messagebox.askokcancel("Fechar", "De certeza que quer sair?"):
                self.window.destroy()
                self.window2.destroy()
                self.window3.destroy()
        self.window.protocol("WM_DELETE_WINDOW", on_closing)  
                
        menubar = Menu(self.window)
        gamemenu = Menu(menubar, tearoff=0)
        gamemenu.add_command(label="Sobre", command=lambda: creditos())
        gamemenu.add_command(label="Sair", command=lambda: quit_program())
        
        menubar.add_cascade(label="Opções", menu=gamemenu)
        menubar.add_cascade(label="Naïve Bayes", command=lambda: menuNaiveBayes())
        menubar.add_cascade(label="Perceptron", command=lambda: menuPerceptron())
        
        self.window.config(menu=menubar)
        self.window.mainloop()