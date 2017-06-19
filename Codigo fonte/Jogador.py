#-------------------------------------------------------------------------------
# Name:        Jogador
# Purpose:     Modulo para as classes que controlam as estruturas do jogador no
#              jogo
#
# Author:      Bruno Iochins Grisci
#
# Created:     07/06/2013
# Copyright:   (c) Bruno Grisci 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random, pygame, sys, math, operator
from pygame.mixer import Sound
from pygame.locals import *
from Componentes import *

class Torre(Componente):
    _ataque = 1
    _TAMANHO_IMAGEM_ORIGINAL = (134,164)
    _dimensao = [134, 164]
    _coordenada = [375, 655]
    _posInicial = [375, 655]
    _FILEPATH = 'Black_Obelisk.png'
    _imagem = pygame.image.load(_FILEPATH)
    _raiodealcance = 200
    _custo = 10
    _audio = pygame.mixer.Sound('Hammering.wav')
    def __init__(self):
        pass
    def getCoordenadaPonta(self):
        return [self._coordenada[0]+38, self._coordenada[1]+1]
    def getRaio(self):
        return self._raiodealcance
    def distancia(self, alvo):
        return math.sqrt(math.pow(self.getCoordenadaPonta()[0] - alvo.getCoordenadaCentral()[0],2) +
                math.pow(self.getCoordenadaPonta()[1] - alvo.getCoordenadaCentral()[1],2))
    def alcancavel(self, alvo):
        if self._raiodealcance >= self.distancia(alvo):
            return True
        else:
            return False
    def getAudio(self):
        return self._audio
    def incAtaque(self):
        if self._ataque < 5:
            self._ataque = self._ataque + 1

class Defesas:
    _defesas = []
    _raiodealcance = 200
    _custo = 10
    _custo_da_bomba = 10
    _cordeexplosao = (255, 255, 153) #Pale Canary Yellow (Crayola Canary)
    _audioexplosao = pygame.mixer.Sound('Big Bomb.wav')
    def __init__(self):
        pass
    def setDefesas(self, lista):
        self._defesas = lista
    def insere(self, torre):
        self._defesas.append(torre)
        torre.getAudio().play()
    def remove(self, torre):
        self._defesas.remove(torre)
    def lista(self):
        return self._defesas
    def getRaio(self):
        return self._raiodealcance
    def getCusto(self):
        return self._custo
    def setCusto(self, valor):
        self._custo = valor
    def ordena(self):
        self._defesas.sort(key = operator.attrgetter('_coordenada'))
    def getCorExplosao(self):
        return self._cordeexplosao
    def getAudioExplosao(self):
        return self._audioexplosao
    def getCustoBomba(self):
        return self._custo_da_bomba
    def bombardeia(self, alvos):
        head = alvos.lista()[0]
        tail = alvos
        tail.remove(head)
        if head.visivel():
            head.danifica()
        if not tail.vazio():
            self.bombardeia(tail)
            tail.insere(head)
        else:
            self._audioexplosao.play()

class Carteira:
    _dinheiro = 20
    def __init__(self):
        pass
    def getDinheiro(self):
        return self._dinheiro
    def setDinheiro(self, valor):
        self._dinheiro = valor
    def compraLiberada(self, item):
         return (lambda x, y: x >= y)(self._dinheiro, item.getCusto())
    def ganhaDinheiro(self, valor):
        self._dinheiro = self._dinheiro + valor
    def gastaDinheiro(self, item):
        if self.compraLiberada(item):
            self._dinheiro = self._dinheiro - item.getCusto()

def main():
    pass

if __name__ == '__main__':
    main()
