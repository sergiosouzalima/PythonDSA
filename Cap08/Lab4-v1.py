# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
from os import system, name

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']



# Função para limar a tela a cada execução
def limpa_tela():

    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')


# Classe
class Hangman:
     TOTAL_CHANCES = 6

     # Método Construtor
     def __init__(self):
          # Lista de palavras para o jogo
          self.palavras = ['banana'] ##, 'abacate', 'uva', 'morango', 'laranja']
          # Escolhe randomicamente uma palavra
          self.palavra = random.choice(self.palavras)
          # Lista  de letras  da palavra
          self.lista_letras_palavras = [letra for letra in self.palavra]
          # Cria o tabuleiro com o caracter "_" multiplicado pelo comprimento da palavra
          self.tabuleiro = ["_"] * len(self.palavra)
          # Número de chances
          self.chances = self.TOTAL_CHANCES
          # Lista para as letras digitadas
          self.letras_tentativas = []

     # Método para adivinhar a letra
     def is_letter_in_drown_word(self, tentativa):
          letter_in_drown_word = tentativa in self.lista_letras_palavras
          if not letter_in_drown_word:
               self.chances -= 1
          self.update_table_of_letters(tentativa)
          return letter_in_drown_word

     # Método para verificar se o jogo terminou
     def is_game_over(self):
         return self.chances <= 0 or self.player_wins()

     # Método para verificar se o jogador venceu
     def player_wins(self):
          return "_" not in self.tabuleiro

     def was_already_tried(self, tentativa):
          return tentativa in self.letras_tentativas

     def add_tried_letters(self, tentativa):
          self.letras_tentativas.append(tentativa)

     # Método para não mostrar a letra no board
     def update_table_of_letters(self, tentativa):
          # update table of letters
          for indice in range(len(self.lista_letras_palavras)):
               if self.lista_letras_palavras[indice] == tentativa:
                    self.tabuleiro[indice] = tentativa

     # Método para checar o status do game e imprimir o board na tela
     def show_board(self):
          print(board[self.TOTAL_CHANCES - self.chances])
          print("\n")

def game():
    limpa_tela()
    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    hangman = Hangman()

    hangman.show_board()

    while not hangman.is_game_over():
          print("Palavra: ", hangman.tabuleiro)
          print("\n")

          # Tentativa
          tentativa = input("\nDigite uma letra: ")

          if hangman.was_already_tried(tentativa):
               print("Você já tentou essa letra. Escolha outra!")
               continue

          hangman.add_tried_letters(tentativa)

          if hangman.is_letter_in_drown_word(tentativa):
               print("Você acertou a letra!")

    if hangman.player_wins():
         print("\nVocê venceu! A palavra era: {}".format(hangman.palavra))
         print("Palavra: ", hangman.tabuleiro)
    else:
         print("\nVocê perdeu! A palavra era: {}.".format(hangman.palavra))

    print("\n")

# Bloco main
if __name__ == "__main__":
    game()
