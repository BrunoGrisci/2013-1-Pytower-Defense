#-------------------------------------------------------------------------------
# Name:        Mapa
# Purpose:     Modulo para os elementos do mapa do jogo
#
# Author:      Bruno Iochins Grisci
#
# Created:     03/06/2013
# Copyright:   (c) Bruno Grisci 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random, pygame, sys
from pygame.locals import *
from Componentes import *

pygame.init()

class Cenario:
    _largura = 880
    _altura = 900
    _cordefundo = (0,128,0) #Verde escuro
    _titulo = 'Pytower Defense'
    _filepathbackground = 'grama.jpg'

    #COORDNADAS DA TELA
    CANTOSUPESQ = (0,       0)
    CANTOSUPDIR = (_largura, 0)
    CANTOINFESQ = (0,  _altura)
    CANTOINFDIR = (_largura, _altura)

    #IMAGEM DE FUNDO
    _gramadefundo = pygame.image.load(_filepathbackground)
    BACKGROUND = pygame.transform.scale(_gramadefundo,(_largura, _altura))

    def __init__(self):
        pass

    def redimensiona(self,larg, alt):
        self._largura = larg
        self._altura = alt

    def getAltura(self):
        return self._altura

    def getLargura(self):
        return self._largura

    def getTitulo(self):
        return self._titulo

    def getCordeFundo(self):
        return self._cordefundo

class Base(Componente):
    _TAMANHO_IMAGEM_ORIGINAL = (0,0)
    _dimensao = [880, 186]
    _posicao = [100, 247]
    _FILEPATH = 'wall.png'
    _FILEPATHdestruicao = 'destrocos.png'
    _imagem = pygame.transform.scale(pygame.image.load(_FILEPATH), _dimensao)
    _imagem_destruicao = pygame.transform.scale(pygame.image.load(_FILEPATHdestruicao), _dimensao)
    _vida = 5500 ##Resistencia da base ate ser destruida
    _ataque = 2
    def __init__(self):
        pass
    def getImagemDestruicao(self):
        return self._imagem_destruicao
    def destruida(self):
        _vida = 0
        _ataque = 0


def main():
    pass

if __name__ == '__main__':
    main()
