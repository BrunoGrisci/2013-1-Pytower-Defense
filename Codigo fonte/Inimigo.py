#-------------------------------------------------------------------------------
# Name:        Inimigo
# Purpose:     Modulo para as classes que controlam os inimigos do jogo
#
# Author:      Bruno Iochins Grisci
#
# Created:     03/06/2013
# Copyright:   (c) Bruno Grisci 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random, pygame, sys, math
from pygame.mixer import Sound
from pygame.locals import *
from Componentes import *

pygame.init()

class Cobra(Componente):

    _TAMANHO_IMAGEM_ORIGINAL = (99,227)
    _dimensao = [99,227]
    _coordenada = [0,0]
    _audiomorte = pygame.mixer.Sound('Bone Crushing.wav')
    _imagem_morte = pygame.image.load('Little dead snake.png')
    _valor = 5

    def andaVertical(self, deslocamento):
        self._coordenada[1] = deslocamento + self._coordenada[1]

    def andaHorizontal(self, deslocamento):
        self._coordenada[0] = deslocamento + self._coordenada[0]

    def getVelocidade(self):
        return self._velocidade

    def getCoordenadaCentral(self):
        return [self._coordenada[0] + math.floor(self._dimensao[0]/2),
                self._coordenada[1] + math.floor(self._dimensao[1]/2)]

    def setVelocidade(self, vel):
        self._velocidade = vel

    def morre(self):
        self._audiomorte.play()
        self._vida = 0
        self._ataque = 0
        self._velocidade = 0
        self._imagem_morte = pygame.transform.scale(self._imagem_morte, self._dimensao)
        self._imagem = self._imagem_morte

    def reduzVelocidade(self):
        self._velocidade = self._velocidade - 1

class CobraLaranja(Cobra):
    _vida = 100
    _velocidade = 5
    _ataque = 1
    _FILEPATH = 'Little orange snake.png'
    _imagem = pygame.image.load(_FILEPATH)
    def __init__(self):
        pass

class CobraAzul(Cobra):
    _vida = 200
    _velocidade = 2
    _ataque = 2
    _FILEPATH = 'Little blue snake.png'
    _imagem = pygame.image.load(_FILEPATH)
    def __init__(self):
        pass

class CobraExplosiva(Cobra):
    _vida = 100
    _velocidade = 3
    _ataque = 10
    _FILEPATH = 'Little bomb snake.png'
    _FILEPATHexplosao = 'Explosion snake.png'
    _imagem = pygame.image.load(_FILEPATH)
    _imagem_morte = pygame.image.load(_FILEPATHexplosao)
    _audiomorte = pygame.mixer.Sound('Grenade.wav')
    def __init__(self):
        pass
    def ataca(self, alvo):
        alvo.danifica(self._ataque)
        self.morre()

class CobraCascuda(Cobra):
    _vida = 400
    _velocidade = 1
    _ataque = 4
    _FILEPATH = 'Little shell snake.png'
    _imagem = pygame.image.load(_FILEPATH)
    _audiomorte = pygame.mixer.Sound('Metal_Drop.wav')
    def __init__(self):
        pass

class CobraEsqueleto(Cobra):
    _vida = 50
    _velocidade = 5
    _ataque = 8
    _FILEPATH = 'Little skull snake.png'
    _imagem = pygame.image.load(_FILEPATH)
    def __init__(self):
        pass

class CobraRobo(Cobra):
    _vida = 300
    _velocidade = 2
    _ataque = 9
    _FILEPATH = 'Little robot snake.png'
    _FILEPATHexplosao = 'Explosion snake.png'
    _imagem = pygame.image.load(_FILEPATH)
    _imagem_morte = pygame.image.load(_FILEPATHexplosao)
    _audiomorte = pygame.mixer.Sound('Grenade.wav')
    def __init__(self):
        pass

class Exercito:
    _horda = []
    def __init__(self):
        pass
    def insere(self, monstro):
        self._horda.append(monstro)
    def remove(self, monstro):
        self._horda.remove(monstro)
    def lista(self):
        return self._horda
    def vazio(self):
        if len(self._horda) == 0:
            return True
        else:
            return False
    def reduzVelocidade(self):
        for cobra in self._horda:
            cobra.reduzVelocidade()
    def setHorda(self, lista):
        self._horda = lista
    def criaHorda(self):
        for i in range(1,random.randrange(1,5)):
            tipo = random.randrange(1,7)
            if tipo == 1:
                cobra = CobraLaranja()
            else:
                if tipo == 2:
                    cobra = CobraAzul()
                else:
                    if tipo == 3:
                        cobra = CobraExplosiva()
                    else:
                        if tipo == 4:
                            cobra = CobraCascuda()
                        else:
                            if tipo == 5:
                                cobra = CobraEsqueleto()
                            else:
                                if tipo == 6:
                                    cobra = CobraRobo()
            cobra.redimensionaProp(1/2)
            pos_x = random.randrange(cobra.getLargura(), 820 - cobra.getLargura())
            pos_y = random.randrange(-5000, -500)
            cobra.setCoordenada(pos_x,pos_y)
            self.insere(cobra)

def main():
    pass

if __name__ == '__main__':
    main()
