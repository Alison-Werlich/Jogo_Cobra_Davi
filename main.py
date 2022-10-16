
import pygame
from pygame.locals import *
from sys import exit
from random import randint

def aumenta_cobra(lista_rastro):
    for XeY in lista_rastro:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, tamanho_cobra, x_cobra, y_cobra, lista_cabeca, lista_rastro
    global x_comida, y_comida, morreu
    pontos = 0
    tamanho_cobra = 5
    x_cobra = int(300)
    y_cobra = int(230)
    lista_cabeca = []
    lista_rastro = []
    x_comida = randint(40, 600)
    y_comida = randint(40, 440)
    morreu = False

pygame.init()      # inicializa o pygame

pygame.mixer.music.set_volume(0.1)                                     # seta altura da musica ( entre 0 e 1 )
musica_de_fundo = pygame.mixer.music.load('sons/music_fundo.mp3')      # carrega musica mp3
pygame.mixer.music.play(-1)                                            # inicializa (-1 para repetir sempre)
som_colisao = pygame.mixer.Sound('sons/coin.wav')                      # carrega o som da colisao


largura_tela = 640                       # largura da tela
altura_tela = 480                        # altura da tela

x_cobra = int(300)                       # posição cobra
y_cobra = int(230)                       # posição cobra

x_controle = 10
y_controle = 0
velocidade = 10

x_comida = randint(40, 600)
y_comida = randint(40, 440)
pontos = 0
tamanho_cobra = 5

lista_rastro = list()
morreu = False

fps = pygame.time.Clock()                                       # cria variavel para o FPS
fonte = pygame.font.SysFont('arial', 30, True, True)            # seta fonte (arial, tamanho, negrito, italico)
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
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0                      #  |
            if event.key == K_d:                        #  |
                if x_controle == - velocidade:
                    pass
                else:
                    x_controle = velocidade             #  |
                    y_controle = 0                      #  | analiza tela precionada e aplica condição
            if event.key == K_w:                        #  |
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0                      #  |
                    y_controle = -velocidade            #  |
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))      # desenha cobra
    comida = pygame.draw.rect(tela, (255,0,0), (x_comida,y_comida,20,20))   # desenha comida


    if cobra.colliderect(comida):
        x_comida = randint(40, 600)                 # se cobra encostar na comida
        y_comida = randint(40, 440)
        pontos = pontos +1
        tamanho_cobra += 1
        som_colisao.play()

    lista_cabeca = list()                          # cria o corpo da cobra
    lista_cabeca.append(x_cobra)                   # baseado na posição atual
    lista_cabeca.append(y_cobra)                   # da cabeça
    lista_rastro.append(lista_cabeca)

    if lista_rastro.count(lista_cabeca) > 1:       # se a cobra encostar nela mesmo

        texto_game_over = fonte.render('Game Over!  Pressione R para reiniciar.', True, (250,250,250))
        morreu = True
        while morreu:
            tela.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()


            tela.blit(texto_game_over, (35, 200))
            pygame.display.update()

    if x_cobra > largura_tela:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura_tela
    if y_cobra > altura_tela:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura_tela


    if len(lista_rastro) > tamanho_cobra:       # se tamanho da lista for maior que o
        del lista_rastro[0]                     # tamanho da cobra, exclui o final da cobra

    aumenta_cobra(lista_rastro)

    tela.blit(placar, (420, 10))                # desenha na tela ( texto renderizado, posição em x, y )

    pygame.display.update()                     # atualiza a tela a cada loop
