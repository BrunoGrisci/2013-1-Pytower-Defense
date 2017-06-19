#-------------------------------------------------------------------------------
# Name:        Pytower_Defense
# Purpose:     Modulo principal do jogo
#
# Author:      Bruno Iochins Grisci
#
# Created:     02/06/2013
# Copyright:   (c) Bruno Iochins Grisci e Jorge Alberto Wagner Filho 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random, pygame, sys, re
import pygame._view
import Mapa, Inimigo, Componentes, Jogador
from pygame.mixer import Sound
from pygame.locals import *

pygame.init()

#FRAMES PER SECOND
FPS = 30 # frames per second
fpsClock = pygame.time.Clock()

mapa = Mapa.Cenario()

#Criando a base do jogador
muralha = Mapa.Base()
muralha.redimensiona()(mapa.getLargura())(muralha.getAltura())
muralha.setCoordenada(0, mapa.getAltura() - muralha.getAltura())

defesas = Jogador.Defesas()
carteira = Jogador.Carteira()

#Criando as cobras inimigas
horda = Inimigo.Exercito()
for i in range(1,10):
    horda.criaHorda()

def main():
    TELADEJOGO = pygame.display.set_mode((mapa.getLargura(), mapa.getAltura()))
    pygame.display.set_caption(mapa.getTitulo())

    contador = [0] #Numero de cobras mortas pelo jogador

    fontObj = pygame.font.Font(pygame.font.get_default_font(), 30)
    textoContador = fontObj.render(str(contador[0])+"+", True, (0,0,0), (0,128,0))
    caixaContador = textoContador.get_rect()
    caixaContador.center = (mapa.getLargura()-caixaContador.center[0], mapa.getAltura()-10)

    #Laco principal do jogo
    while True:

        TELADEJOGO.fill(mapa.getCordeFundo())
        TELADEJOGO.blit(mapa.BACKGROUND, mapa.CANTOSUPESQ)

        if horda.lista() != []:
            for cobra in horda.lista():
                if(cobra.estaVivo()):
                    if (cobra.getPosY() < (mapa.getAltura() - muralha.getAltura()) or (not muralha.estaVivo())):
                        cobra.andaVertical(cobra.getVelocidade())
                    else:
                        if muralha.estaVivo():
                            cobra.ataca(muralha)
                            muralha.ataca(cobra)
                    if cobra.getPosY() > mapa.getAltura():
                        horda.remove(cobra)
                        horda.criaHorda()
                    TELADEJOGO.blit(cobra.getImagem(), cobra.getCoordenada())
                #Cobra morta
                else:
                    cobra.morre()
                    TELADEJOGO.blit(cobra.getImagem(), cobra.getCoordenada())
                    carteira.ganhaDinheiro(cobra.getValor())
                    horda.remove(cobra)
                    horda.criaHorda()
                    if muralha.estaVivo():
                        contador = list(map(lambda x: x+1, contador))

        #Desenha torres
        defesas.ordena()
        for torre in defesas.lista():
            TELADEJOGO.blit(torre.getImagem(), torre.getCoordenada())

        #Trata os eventos de mouse e teclado
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #Desenha area de construcao quando jogador possui dinheiro suficiente
            if(pygame.mouse.get_pressed() and pygame.mouse.get_pos()[1] < muralha.getCoordenada()[1] and carteira.getDinheiro() >= defesas.getCusto()
                                            and muralha.estaVivo()):
                tela = TELADEJOGO.convert_alpha()
                pygame.draw.circle(tela, (125,0,0,127), pygame.mouse.get_pos(), defesas.getRaio())
                TELADEJOGO.blit(tela,(0,0))
            #Cria nova torre
            if(pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[1] < muralha.getCoordenada()[1]):
                t = Jogador.Torre()
                if carteira.compraLiberada(defesas) and muralha.estaVivo():
                    t.setCoordenada(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                    defesas.insere(t)
                    carteira.gastaDinheiro(defesas)
                    defesas.setCusto(defesas.getCusto() + t.getCusto())
            #Aumenta o ataque das torres
            if(pygame.mouse.get_pressed()[2] and carteira.compraLiberada(defesas) and muralha.estaVivo() and defesas.lista() != []):
                def incrementa(x):
                    x.incAtaque()
                    return x
                defesas.setDefesas(list(map(incrementa, defesas.lista())))
                carteira.gastaDinheiro(defesas)
                defesas.setCusto(defesas.getCusto() + t.getCusto())
            #Joga bomba
            if(pygame.key.get_pressed()[K_SPACE] and carteira.compraLiberada(defesas) and muralha.estaVivo()):
                defesas.bombardeia(horda)
                carteira.gastaDinheiro(defesas)
                defesas.setCusto(defesas.getCusto() + defesas.getCustoBomba())
                TELADEJOGO.fill(defesas.getCorExplosao())

        #Ataque das torres
        if muralha.estaVivo():
            for torre in defesas.lista():
                for cobra in horda.lista():
                    if cobra.visivel() and torre.alcancavel(cobra):
                        pygame.draw.line(TELADEJOGO, (255,0,0), (torre.getCoordenadaPonta()), cobra.getCoordenadaCentral(), torre.getAtaque())
                        torre.ataca(cobra)
                        break

        #Atualiza muralha
        if muralha.estaVivo():
            TELADEJOGO.blit(muralha.getImagem(), muralha.getCoordenada())
        else:
            TELADEJOGO.blit(muralha.getImagemDestruicao(), muralha.getCoordenada())
            muralha.destruida()

        #Desenha numero de cobras mortas na tela
        textoContador = fontObj.render(str(contador[0])+"+", True, (0,0,0), (200,0,0))
        caixaContador = textoContador.get_rect()
        caixaContador.center = (mapa.getLargura()-caixaContador.center[0], mapa.getAltura()-10)
        TELADEJOGO.blit(textoContador, caixaContador)

        #Desenha quantidade de dinheiro na carteira na tela
        textoCarteira = fontObj.render(str(carteira.getDinheiro())+"$", True, (0,0,0), (255, 255, 0))
        caixaCarteira = textoCarteira.get_rect()
        caixaCarteira.center = (mapa.getLargura()-caixaCarteira.center[0], caixaContador.center[1]-35)
        TELADEJOGO.blit(textoCarteira, caixaCarteira)

        #Desenha vida restante da muralha na tela
        textoHP = fontObj.render(str(muralha.getVida())+"HP", True, (0,0,0), (0, 128, 0))
        caixaHP = textoCarteira.get_rect()
        caixaHP.center = (40, mapa.getAltura()-15)
        TELADEJOGO.blit(textoHP, caixaHP)

        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()
