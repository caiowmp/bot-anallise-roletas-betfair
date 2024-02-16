LOGIN = "teste@gmail.com"
SENHA = "teste123?"
QUANTIDADE_PADRAO = 6

NUMEROS_PARES = [str(num) for num in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]]
NUMEROS_IMPARES = [str(num) for num in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]]
NUMEROS_ALTOS = [str(num) for num in [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]]
NUMEORS_BAIXOS = [str(num) for num in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]]
NUMEROS_VERMELHOS = [str(num) for num in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]]
NUMEROS_PRETOS = [str(num) for num in [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]]

import tkinter as tk
from tkinter import simpledialog

# Função para exibir uma notificação com uma janela de entrada de texto
def exibir_notificacao():
  global QUANTIDADE_PADRAO
  root = tk.Tk()
  root.withdraw()  # Oculta a janela principal
  root.option_add("*Font", "Arial 12")  # Altera a fonte para Arial tamanho 12
  root.option_add("*Background", "#f0f0f0")  # Altera a cor de fundo para cinza claro
  root.option_add("*Foreground", "#333333")
  entrada = simpledialog.askstring("Notificação com Textbox", "Digite o texto da notificação:")
  if entrada:
    QUANTIDADE_PADRAO = int(entrada)
