# 🧠 Jogo da Memória em Python

Este projeto é um jogo da memória desenvolvido em Python utilizando a biblioteca Tkinter para interface gráfica.

## Funcionalidades

- Escolha do tamanho do tabuleiro:
  - 4x4
  - 6x6
  - 8x8
- Sistema de temas (cores personalizadas via JSON)
- Contador de jogadas
- Feedback visual:
  - Verde para acerto
  - Vermelho para erro
- Reiniciar partida
- Voltar ao menu inicial
- Detecção de vitória

## Como funciona

O jogador deve encontrar pares de cartas iguais. Ao clicar em duas cartas:
- Se forem iguais → permanecem abertas
- Se forem diferentes → são escondidas novamente após um curto tempo

O jogo termina quando todos os pares são encontrados.

## Tecnologias utilizadas

- Python 3
- Tkinter (interface gráfica)
- JSON (configuração de temas)