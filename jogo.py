import tkinter as tk
import random


#var globais
primeira_carta = None
segunda_carta = None
travado = False


def init_jogo(nome:str, tema, tamanho:int, janela_menu):
    #var jogo
    global tabuleiro, cartas, janela, cor_tema, label_status, label_jogadas
    global primeira_carta, segunda_carta, travado
    global jogadas

    jogadas = 0

    primeira_carta = None
    segunda_carta = None
    travado = False

    nome_jogo = nome

    cor_tema = tema # cores do jogo

    tamanho_grid = tamanho

    #janela
    janela = tk.Toplevel()
    janela.title(f'{nome_jogo} - {tamanho_grid}X{tamanho_grid}')
    janela.configure(bg=cor_tema['fundo'])

    # Titulo jogo
    titulo = tk.Label(janela,text=nome_jogo,fg=cor_tema['titulo'],font=("Arial", 20, "bold"))
    titulo.grid(row=0, column=0, columnspan=tamanho_grid)

    #placar
    label_jogadas = tk.Label(janela, text="Jogadas : 0", font=("Arial", 18, "bold"), fg=cor_tema['texto'])
    label_jogadas.grid(row=1, column=0, columnspan=tamanho_grid)

    #reinicia
    tk.Button(janela,text="Reiniciar",font=("Arial", 18, "bold"), fg=cor_tema['texto'], command=lambda:reiniciar(nome_jogo,cor_tema,tamanho_grid, janela_menu)
              ).grid(row=tamanho+3, column=0, columnspan=tamanho_grid//2)
    
    #voltar ao menu
    tk.Button(janela,text="Voltar ao Menu",font=("Arial", 18, "bold"), fg=cor_tema['texto'], command=lambda:voltar_menu(janela,janela_menu)
              ).grid(row=tamanho+3, column=tamanho_grid//2, columnspan=tamanho_grid//2)

    #Texto de vitoria
    label_status = tk.Label(janela, text="", font=("Arial", 20, "bold"), fg="#f1c40f")
    label_status.grid(row=+2, column=0, columnspan=tamanho_grid)

    #cartas
    cartas = [] #lista de Cartas

    # gerar pares
    total_cartas = tamanho_grid * tamanho_grid
    total_pares = total_cartas // 2
    valores = []

    for i in range(total_pares):
        valores.append(str(i))
        valores.append(str(i))
    
    random.shuffle(valores) # randomiza a lista

    # criar tabuleiro
    tabuleiro = []
    for i in range(tamanho_grid):
        linha = valores[i*tamanho_grid:(i+1)*tamanho_grid]
        tabuleiro.append(linha)

    #grid
    for linha in range(tamanho_grid):
        linha_botoes = []
        for coluna in range(tamanho_grid):
            #botões que vão ser as cartas
            botao = tk.Button(janela,text='?',width=6,height=2,bg=cor_tema['carta'],fg=cor_tema['carta_texto'],font=("Arial", 20, "bold"), command = lambda l=linha, c=coluna: clicar(l,c))

            botao.grid(row=linha+3, column=coluna, padx=2, pady=2)
            linha_botoes.append(botao)
        
        cartas.append(linha_botoes)


def clicar(linha, coluna):
    global primeira_carta, segunda_carta, travado

    if travado:
        return
    
    botao = cartas[linha][coluna]

    if botao["text"] != "?":
        return
    
    valor = tabuleiro[linha][coluna]
    botao.config(text=valor)

    if primeira_carta is None:
        primeira_carta = (linha, coluna)

    elif segunda_carta is None:
        segunda_carta = (linha,coluna)
        verificar()


def verificar():
    global primeira_carta, segunda_carta, travado, jogadas

    l1, c1 = primeira_carta
    l2, c2 = segunda_carta

    v1 = tabuleiro[l1][c1]
    v2 = tabuleiro[l2][c2]

    if v1 == v2:
        cartas[l1][c1].config(bg="#2ecc71")  # verde
        cartas[l2][c2].config(bg="#2ecc71")  # verde

        primeira_carta = None
        segunda_carta = None

        verificar_vitoria()
    else:
        cartas[l2][c2].config(bg="#e74c3c")  # vermelho
        cartas[l2][c2].config(bg="#e74c3c")  # vermelho

        travado = True
        janela.after(1000, esconder)

    jogadas += 1
    label_jogadas.config(text=f"Jogadas: {jogadas}")


def esconder():
    global primeira_carta, segunda_carta, travado

    l1, c1 = primeira_carta
    l2, c2 = segunda_carta

    cartas[l1][c1].config(text="?", bg=cor_tema['carta'])
    cartas[l2][c2].config(text="?", bg=cor_tema['carta'])

    primeira_carta = None
    segunda_carta = None
    travado = False


def verificar_vitoria():
    for linhas in cartas:
        for botoa in linhas:
            if botoa["text"] == "?":
                return
    
    venceu()


def venceu():
    label_status.config(text="Vitoria!")


def reiniciar(nome:str, tema, tamanho:int, janela_menu):
    janela.destroy()
    init_jogo(nome, tema, tamanho, janela_menu)


def voltar_menu(janela_jogo,janela_menu):
    janela_jogo.destroy()
    janela_menu.deiconify()
