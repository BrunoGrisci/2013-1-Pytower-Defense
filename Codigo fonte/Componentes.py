#-------------------------------------------------------------------------------
# Name:        Componentes
# Purpose:     Modulo para a classe abstrata Componente que Ã© herdada por
#              diversas outras classes e possui atributos e metodos genericos
#
# Author:      Bruno Iochins Grisci
#
# Created:     03/06/2013
# Copyright:   (c) Bruno Grisci 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random, pygame, sys, math
from pygame.locals import *

pygame.init()

class Componente:

    _TAMANHO_IMAGEM_ORIGINAL = (0,0)
    _dimensao = [0, 0]
    _vida = 0
    _ataque = 0
    _coordenada = [0, 0]
    _posInicial = [0, 0]
    _FILEPATH = ' '
    _imagem = None
    _valor = 0
    _custo = 0

    #Exemplo de currying simulado em Python
    def redimensiona(self):
        def redimensionaLargura(larg):
            def redimensionaAltura(alt):
                self._altura = alt
                self._largura = larg
            return redimensionaAltura
        return redimensionaLargura

    def redimensionaProp(self, escala):
        if escala > 0:
            self._dimensao = [math.floor(self._dimensao[0]*escala),
                               math.floor(self._dimensao[1]*escala)]
            self._imagem = pygame.transform.scale(self._imagem, self._dimensao)

    def atualizaVida(self, hp):
        self._vida = hp

    def getVida(self):
        return self._vida

    def danifica(self, dano=300):
        self._vida = self._vida - dano

    def getImagem(self):
        return self._imagem

    def getCoordenada(self):
        return self._coordenada

    def setCoordenada(self, x, y):
        self._coordenada = [x, y]

    def setPosX(self, x):
        self._coordenada[0] = x

    def setPosY(self, y):
        self._coordenada[1] = y

    def getPosX(self):
        return self._coordenada[0]

    def getPosY(self):
        return self._coordenada[1]

    def getPosInicial(self):
        return self._posInicial

    def setPosInical(self, posicao):
        self._posInicial = posicao

    def setFilepath(self, filepath):
        self._FILEPATH = filepath

    def getFilepath(self):
        return self._FILEPATH

    def setTamanhoImagemOriginal(self, tamanho):
        self._TAMANHO_IMAGEM_ORIGINAL = tamanho

    def setImagem(self, imagem):
        self._imagem = pygame.transform.scale(imagem, self._dimensao)

    def getAltura(self):
        return self._dimensao[1]

    def getLargura(self):
        return self._dimensao[0]

    def estaVivo(self):
        if self._vida > 0:
            return True
        else:
            return False

    def setAtaque(self, atk):
        self._ataque = atk

    def getAtaque(self):
        return self._ataque

    def incAtaque(self):
        self._ataque = self._ataque + 1

    def ataca(self, alvo):
        alvo.danifica(self._ataque)

    def clicado(self, mouse_pos):
        if mouse_pos[0] < self._coordenada[0] + self._dimensao[0]:
            if mouse_pos[0] > self._coordenada[0] - self._dimensao[0]:
                if mouse_pos[1] < self._coordenada[1] + self._dimensao[1]:
                    if mouse_pos[1] > self._coordenada[1] - self._dimensao[1]:
                        return True
        return False

    def morre(self):
        self._ataque = 0
        self._vida = 0

    def visivel(self):
        if self._coordenada[0] > 0 and self._coordenada[0] < 880:
            if self._coordenada[1] > 0 and self._coordenada[1] < 900:
                return True
        return False

    def getCusto(self):
        return self._custo
    def getValor(self):
        return self._valor

def main():
    pass

if __name__ == '__main__':
    main()

