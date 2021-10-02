##Importa a pasta
import pygame
from random import randint

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green =(0,255,0)
blue =(0,0,255)
##Verificando se a biblioteca iniciou corretamente
try:
    pygame.init()
except:
    print('O moduulo nao foi inicializado')
#declaração dessas variaveis caso use dps
largura= 320
altura = 240
tamanho = 10


relogio= pygame.time.Clock()
## define o tamanho da tela

fundo = pygame.display.set_mode((largura, altura))
imag= pygame.image.load('a.jfif')

fundo.blit(imag, (0, 0))
pygame.display.update()