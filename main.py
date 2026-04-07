import tkinter as tk
import jogo
import json


def iniciar():
    valor = tamanho_jogo.get()
    tamanho = int(valor.split("x")[0])
    tema = temas[cor_tema.get()]

    janela_init.withdraw()
    jogo.init_jogo(nome_jogo,tema,tamanho, janela_init)


# var para o jogo
nome_jogo = "Jogo da Memória"

with open("temas.json", "r") as joson_tema:
    temas = json.load(joson_tema)

#janela
janela_init = tk.Tk()
janela_init.title(nome_jogo)
janela_init.geometry("500x300")

tamanho_jogo = tk.StringVar()
tamanho_jogo.set("4x4")

cor_tema = tk.StringVar()
cor_tema.set(list(temas.keys())[0]) # define o primeiro como padrão

botao_tamanho_jogo = tk.OptionMenu(janela_init,tamanho_jogo, "4x4", "6x6", "8x8")
botao_tamanho_jogo.config(font=("Arial", 18, "bold"), padx=50, pady=10, fg="#44403C", bg="#FDBA74")
botao_tamanho_jogo.pack()

botao_tema = tk.OptionMenu(janela_init,cor_tema, *temas.keys())
botao_tema.config(font=("Arial", 18, "bold"), padx=50, pady=10, fg="#44403C", bg="#FDBA74")
botao_tema.pack()

botao_init = tk.Button(janela_init, text="Iniciar Jogo", command=iniciar)
botao_init.config(font=("Arial", 18, "bold"), padx=100, pady=10, fg="#44403C", bg="#FDBA74")
botao_init.pack()

janela_init.mainloop()
