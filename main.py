
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()      # inicializa o pygame

largura_tela = 640                 # largura da tela
altura_tela = 480                  # altura da tela
x = 300                            # posição
y = 230                            # posição
x_comida = randint(40, 600)
y_comida = randint(40, 440)
pontos = 0

fps = pygame.time.Clock()                                       # cria variavel para o FPS
fonte = pygame.font.SysFont('arial', 40, True, True)            # seta fonte (arial, tamanho, negrito, italico)
tela = pygame.display.set_mode((largura_tela, altura_tela))     # cria a tela
pygame.display.set_caption('Davi Game Cobrinha')                # cria um nome para a janela

while True:                                             # looping infinito do jogo

    fps.tick(30)                                        # seta o FPS
    tela.fill((0,0,0))                                  # preenche a tela a cada loop para nao ficar rastro

    msg = f'Pontos: {pontos}'                           # cria mensagem a ser exibida
    placar = fonte.render(msg, True, (255, 255, 255))   # cria a msg formatada ( msg, antiallising, cor )

    for event in pygame.event.get():                    # para cada evento no loop
        if event.type == QUIT:                          # se evento for clicar no X da janela
            pygame.quit()                               # encerrar pygame
            exit()                                      # fechar janela

        if event.type == KEYDOWN:                       # se evento for apertar uma tecla
            if event.key == K_a:
                x = x - 20                          #  |
            if event.key == K_d:                    #  |
                x = x + 20                          #  | analiza tela precionada e aplica condição
            if event.key == K_w:                    #  |
                y = y -20                           #  |
            if event.key == K_s:
                y = y + 20

    cobra = pygame.draw.rect(tela, (255,0,0), (x,y,40,40))                  # desenha cobra
    comida = pygame.draw.rect(tela, (0,0,255), (x_comida,y_comida,40,40))   # desenha comida

    if cobra.colliderect(comida):
        x_comida = randint(40, 600)                 # se cobra encostar na comida
        y_comida = randint(40, 440)
        pontos = pontos +1

    tela.blit(placar, (450, 40))                    # desenha na tela ( texto renderizado, posição em x, y )

    pygame.display.update()                         # atualiza a tela a cada loop
