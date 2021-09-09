from tkinter import *
from tkinter import messagebox
from solver import solve, solve2, sudoku, fetch_sudokus, value, value2, sudoku_aleat, criar_sudoku, get_time
import time

colunas = ("ABCDEFGHI")

A1 = A2 = A3 = A4 = A5 = A6 = A7 = A8 = A9 = None
B1 = B2 = B3 = B4 = B5 = B6 = B7 = B8 = B9 = None
C1 = C2 = C3 = C4 = C5 = C6 = C7 = C8 = C9 = None
D1 = D2 = D3 = D4 = D5 = D6 = D7 = D8 = D9 = None
E1 = E2 = E3 = E4 = E5 = E6 = E7 = E8 = E9 = None
F1 = F2 = F3 = F4 = F5 = F6 = F7 = F8 = F9 = None
G1 = G2 = G3 = G4 = G5 = G6 = G7 = G8 = G9 = None
H1 = H2 = H3 = H4 = H5 = H6 = H7 = H8 = H9 = None
I1 = I2 = I3 = I4 = I5 = I6 = I7 = I8 = I9 = None

class GUI:
    def __init__(self):
        self.root = Tk()       
        self.root.title("Sudoku")

        frame1 = LabelFrame(self.root, padx=1, pady=1, borderwidth = 0, highlightthickness = 0, bg="#555555")
        frame2 = LabelFrame(self.root, padx=1, pady=1, borderwidth = 0, highlightthickness = 0, bg="#555555")
        frame3 = LabelFrame(self.root, padx=1, pady=1, borderwidth = 0, highlightthickness = 0, bg="#555555")
        frame4 = LabelFrame(self.root, padx=1, pady=1, borderwidth = 0, highlightthickness = 0, bg="#555555")
        frame5 = LabelFrame(self.root, padx=1, pady=1, borderwidth = 0, highlightthickness = 0, bg="#555555")
        frame6 = LabelFrame(self.root, padx=1, pady=1, borderwidth = 0, highlightthickness = 0, bg="#555555")
        frame7 = LabelFrame(self.root, padx=1, pady=1, borderwidth = 0, highlightthickness = 0, bg="#555555")
        frame8 = LabelFrame(self.root, padx=1, pady=1, borderwidth = 0, highlightthickness = 0, bg="#555555")
        frame9 = LabelFrame(self.root, padx=1, pady=1, borderwidth = 0, highlightthickness = 0, bg="#555555")

        def display_frames():   # Função que disponibiliza as nove frames do sudoku, no tkinter.
            frame1.grid(row = 0, column = 0)
            frame2.grid(row = 0, column = 1)
            frame3.grid(row = 0, column = 2)
            frame4.grid(row = 1, column = 0)
            frame5.grid(row = 1, column = 1)
            frame6.grid(row = 1, column = 2)
            frame7.grid(row = 2, column = 0)
            frame8.grid(row = 2, column = 1)
            frame9.grid(row = 2, column = 2)
        display_frames()

        global A1, A2, A3, A4, A5, A6, A7, A8, A9, B1, B2, B3, B4, B5, B6, B7, B8, B9
        global C1, C2, C3, C4, C5, C6, C7, C8, C9, D1, D2, D3, D4, D5, D6, D7, D8, D9
        global E1, E2, E3, E4, E5, E6, E7, E8, E9, F1, F2, F3, F4, F5, F6, F7, F8, F9
        global G1, G2, G3, G4, G5, G6, G7, G8, G9, H1, H2, H3, H4, H5, H6, H7, H8, H9
        global I1, I2, I3, I4, I5, I6, I7, I8, I9

        #Frame 1
        A1 = Canvas(frame1, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        A2 = Canvas(frame1, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        A3 = Canvas(frame1, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        B1 = Canvas(frame1, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        B2 = Canvas(frame1, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        B3 = Canvas(frame1, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        C1 = Canvas(frame1, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        C2 = Canvas(frame1, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        C3 = Canvas(frame1, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")

        #Frame 2
        A4 = Canvas(frame2, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        A5 = Canvas(frame2, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        A6 = Canvas(frame2, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        B4 = Canvas(frame2, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        B5 = Canvas(frame2, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        B6 = Canvas(frame2, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        C4 = Canvas(frame2, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        C5 = Canvas(frame2, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        C6 = Canvas(frame2, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")

        #Frame 3
        A7 = Canvas(frame3, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        A8 = Canvas(frame3, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        A9 = Canvas(frame3, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        B7 = Canvas(frame3, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        B8 = Canvas(frame3, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        B9 = Canvas(frame3, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        C7 = Canvas(frame3, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        C8 = Canvas(frame3, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        C9 = Canvas(frame3, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")

        #Frame 4
        D1 = Canvas(frame4, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        D2 = Canvas(frame4, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        D3 = Canvas(frame4, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        E1 = Canvas(frame4, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        E2 = Canvas(frame4, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        E3 = Canvas(frame4, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        F1 = Canvas(frame4, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        F2 = Canvas(frame4, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        F3 = Canvas(frame4, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")

        #Frame 5
        D4 = Canvas(frame5, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        D5 = Canvas(frame5, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        D6 = Canvas(frame5, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        E4 = Canvas(frame5, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        E5 = Canvas(frame5, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        E6 = Canvas(frame5, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        F4 = Canvas(frame5, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        F5 = Canvas(frame5, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        F6 = Canvas(frame5, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")

        #Frame 6
        D7 = Canvas(frame6, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        D8 = Canvas(frame6, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        D9 = Canvas(frame6, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        E7 = Canvas(frame6, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        E8 = Canvas(frame6, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        E9 = Canvas(frame6, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        F7 = Canvas(frame6, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        F8 = Canvas(frame6, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        F9 = Canvas(frame6, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")

        #Frame 7
        G1 = Canvas(frame7, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        G2 = Canvas(frame7, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        G3 = Canvas(frame7, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        H1 = Canvas(frame7, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        H2 = Canvas(frame7, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        H3 = Canvas(frame7, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        I1 = Canvas(frame7, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        I2 = Canvas(frame7, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        I3 = Canvas(frame7, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")

        #Frame 8
        G4 = Canvas(frame8, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        G5 = Canvas(frame8, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        G6 = Canvas(frame8, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        H4 = Canvas(frame8, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        H5 = Canvas(frame8, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        H6 = Canvas(frame8, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        I4 = Canvas(frame8, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        I5 = Canvas(frame8, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        I6 = Canvas(frame8, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")

        #Frame 9
        G7 = Canvas(frame9, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        G8 = Canvas(frame9, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        G9 = Canvas(frame9, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        H7 = Canvas(frame9, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        H8 = Canvas(frame9, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        H9 = Canvas(frame9, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        I7 = Canvas(frame9, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        I8 = Canvas(frame9, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")
        I9 = Canvas(frame9, bg = 'White', width = 55, height = 55, highlightthickness=1, highlightbackground = "#d3d3d3")

        def display_canvas():   # Função que disponibiliza a ordem de cada quadrado (Coluna, Linha) dentro de cada frame
            #Frame 1
            A1.grid(row = 0, column = 0)
            A2.grid(row = 0, column = 1)
            A3.grid(row = 0, column = 2)
            B1.grid(row = 1, column = 0)
            B2.grid(row = 1, column = 1)
            B3.grid(row = 1, column = 2)
            C1.grid(row = 2, column = 0)
            C2.grid(row = 2, column = 1)
            C3.grid(row = 2, column = 2)

            #Frame 2
            A4.grid(row = 0, column = 0)
            A5.grid(row = 0, column = 1)
            A6.grid(row = 0, column = 2)
            B4.grid(row = 1, column = 0)
            B5.grid(row = 1, column = 1)
            B6.grid(row = 1, column = 2)
            C4.grid(row = 2, column = 0)
            C5.grid(row = 2, column = 1)
            C6.grid(row = 2, column = 2)                        

            #Frame 3
            A7.grid(row = 0, column = 0)
            A8.grid(row = 0, column = 1)
            A9.grid(row = 0, column = 2)
            B7.grid(row = 1, column = 0)
            B8.grid(row = 1, column = 1)
            B9.grid(row = 1, column = 2)
            C7.grid(row = 2, column = 0)
            C8.grid(row = 2, column = 1)
            C9.grid(row = 2, column = 2)            

            #Frame 4
            D1.grid(row = 0, column = 0)
            D2.grid(row = 0, column = 1)
            D3.grid(row = 0, column = 2)
            E1.grid(row = 1, column = 0)
            E2.grid(row = 1, column = 1)
            E3.grid(row = 1, column = 2)
            F1.grid(row = 2, column = 0)
            F2.grid(row = 2, column = 1)
            F3.grid(row = 2, column = 2)                       

            #Frame 5
            D4.grid(row = 0, column = 0)
            D5.grid(row = 0, column = 1)
            D6.grid(row = 0, column = 2)
            E4.grid(row = 1, column = 0)
            E5.grid(row = 1, column = 1)
            E6.grid(row = 1, column = 2)
            F4.grid(row = 2, column = 0)
            F5.grid(row = 2, column = 1)
            F6.grid(row = 2, column = 2)

            #Frame 6
            D7.grid(row = 0, column = 0)
            D8.grid(row = 0, column = 1)
            D9.grid(row = 0, column = 2)
            E7.grid(row = 1, column = 0)
            E8.grid(row = 1, column = 1)
            E9.grid(row = 1, column = 2)
            F7.grid(row = 2, column = 0)
            F8.grid(row = 2, column = 1)
            F9.grid(row = 2, column = 2)                        

            #Frame 7
            G1.grid(row = 0, column = 0)
            G2.grid(row = 0, column = 1)
            G3.grid(row = 0, column = 2)
            H1.grid(row = 1, column = 0)
            H2.grid(row = 1, column = 1)
            H3.grid(row = 1, column = 2)
            I1.grid(row = 2, column = 0)
            I2.grid(row = 2, column = 1)
            I3.grid(row = 2, column = 2)                        

            #Frame 8
            G4.grid(row = 0, column = 0)
            G5.grid(row = 0, column = 1)
            G6.grid(row = 0, column = 2)
            H4.grid(row = 1, column = 0)
            H5.grid(row = 1, column = 1)
            H6.grid(row = 1, column = 2)
            I4.grid(row = 2, column = 0)
            I5.grid(row = 2, column = 1)
            I6.grid(row = 2, column = 2)                        

            #Frame 9
            G7.grid(row = 0, column = 0)
            G8.grid(row = 0, column = 1)
            G9.grid(row = 0, column = 2)
            H7.grid(row = 1, column = 0)
            H8.grid(row = 1, column = 1)
            H9.grid(row = 1, column = 2)
            I7.grid(row = 2, column = 0)
            I8.grid(row = 2, column = 1)
            I9.grid(row = 2, column = 2)
        display_canvas()

        def button_sudoku():   # Função para preencher cada quadrado do sudoku, com os valores do sudoku proposto do ficheiro solver
            button_clear()
            i_sudoku = sudoku
            for c in colunas:
                for l in range(1, 10):                                                    
                    canvas_id = eval(c+str(l)).create_text(25, 20, anchor="nw")
                    if i_sudoku[0]=="0":
                        eval(c+str(l)).itemconfig(canvas_id, text = " ", tag=(c+str(l)))
                        i_sudoku = i_sudoku[1:]
                    else:
                        eval(c+str(l)).itemconfig(canvas_id, text = i_sudoku[0], tag=(c+str(l)))
                        i_sudoku = i_sudoku[1:]
                        
        def button_sudoku_aleat():   # Função para preencher cada quadrado do sudoku, com os valores do sudoku aleatório gerado no ficheiro solver
            button_clear()
            i_sudoku = sudoku_aleat
            for c in colunas:
                for l in range(1, 10):                                                    
                    canvas_id = eval(c+str(l)).create_text(25, 20, anchor="nw")
                    if i_sudoku[0]=="0":
                        eval(c+str(l)).itemconfig(canvas_id, text = " ", tag=(c+str(l)))
                        i_sudoku = i_sudoku[1:]
                    else:
                        eval(c+str(l)).itemconfig(canvas_id, text = i_sudoku[0], tag=(c+str(l)))
                        i_sudoku = i_sudoku[1:]

        def button_clear():   # Função que limpa todos os valores de cada célula mostrados anteriormente, na aplicação  tkinter
            for c in colunas:
                for l in range(1, 10):                    
                    canvas_id = eval(c+str(l)).create_text(25, 20, anchor="nw")
                    eval(c+str(l)).delete((c+str(l)))

        def button_resolution():   # Função para preencher cada quadrado do sudoku com os valores totais do sudoku proposto
            sudoku_grid_as_string = sudoku
            
            sudoku_queue = fetch_sudokus(sudoku_grid_as_string)
        
            for index, sudoku_grid in enumerate(sudoku_queue):
                solve(sudoku_grid, index, len(sudoku_queue))

            f_sudoku = value
            button_clear()
            for c in colunas:                
                for l in range(1, 10):                    
                    canvas_id = eval(c+str(l)).create_text(25, 20, anchor="nw")
                    eval(c+str(l)).itemconfig(canvas_id, text = f_sudoku[0], tag=(c+str(l)))
                    f_sudoku = f_sudoku[1:]
                    eval(c+str(l)).update()
                    
        def button_resolution2():   # Função para preencher cada quadrado do sudoku com os valores totais do sudoku gerado aleatoriamente
            sudoku_grid_as_string2 = sudoku_aleat
        
            sudoku_queue = fetch_sudokus(sudoku_grid_as_string2)
        
            for index, sudoku_grid in enumerate(sudoku_queue):
                solve2(sudoku_grid, index, len(sudoku_queue))

            f_sudoku = value2
            button_clear()
            
            if not value2:
                messagebox.showerror(title="Erro", message="Este Sudoku não tem resultado com o AC3")
                
            else:
                for c in colunas:                
                    for l in range(1, 10):                    
                        canvas_id = eval(c+str(l)).create_text(25, 20, anchor="nw")
                        eval(c+str(l)).itemconfig(canvas_id, text = f_sudoku[0], tag=(c+str(l)))
                        f_sudoku = f_sudoku[1:]
                        eval(c+str(l)).update()
        
        def creditos():    # Função que mostra os créditos do trabalho
            messagebox.showinfo('Créditos',"""  
            Elaborado por:                         
                                                    
             - {:20s}       -   Nº 30003769       
             - {:20s}   -   Nº 30003043       
             - {:20s}   -   Nº 30005711       
             - {:20s}    -   Nº 30003039       
                                                    
                    Inteligência Artificial        
             @UAL - Universidade Autónoma de Lisboa     
            """.format('Bruno Silva', 'David Monteiro', 'Nuno Barrocas', 'Zacarias Chiena'))
            
        def quit_program():   # Função para sair do programa
            self.root.quit()
            self.root.destroy()
        
        def on_closing():   # Função para sair do programa, clicando no X, na parte superior direita
            if messagebox.askokcancel("Fechar", "De certeza que quer sair?"):
                self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)
        
        menubar = Menu(self.root)
        
        gamemenu = Menu(menubar, tearoff=0)
        gamemenu.add_command(label="Sobre", command=lambda: creditos())
        gamemenu.add_command(label="Limpar", command=lambda: button_clear())
        gamemenu.add_command(label="Sair", command=lambda: quit_program())
        
        menubar.add_cascade(label="Opções", menu=gamemenu)
        menubar.add_cascade(label="Figura 1", command=lambda: button_sudoku())
        menubar.add_cascade(label="Solução", command=lambda: button_resolution())
        menubar.add_cascade(label="Gerar Sudoku", command=lambda: button_sudoku_aleat())
        menubar.add_cascade(label="Solução", command=lambda: button_resolution2())
        
        self.root.config(menu=menubar)
        self.root.mainloop()