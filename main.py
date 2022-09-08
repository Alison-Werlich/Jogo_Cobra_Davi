
import pygame
from pygame.locals import *
from sys import exit


pygame.init()      # inicializa o pygame

largura = 640      # largura da tela
altura = 480       # altura da tela

tela = pygame.display.set_mode((largura, altura))   # cria a tela
pygame.display.set_caption('Davi Game Cobrinha')    # cria um nome para a janela

while True:                                         # looping infinito do jogo
    for event in pygame.event.get():                # para cada evento no loop
        if event.type == QUIT:                      # se evento for clicar no X da janela
            pygame.quit()                           # encerrar pygame
            exit()                                  # fechar janela
    
    pygame.display.update()                         # atualiza a tela a cada loop
