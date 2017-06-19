#-------------------------------------------------------------------------------
# Name:        setup
# Purpose:     Modulo para a criacao de um arquivo executavel do jogo
#
# Author:      Bruno Iochins Grisci
#
# Created:     06/06/2013
# Copyright:   (c) Bruno Grisci 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame._view
import re
from cx_Freeze import setup, Executable

exe= Executable(
        script="Pytower_Defense.py",
        base="Win32Gui",
     )
includes = ["sys","random","pygame","math","pygame._view","pygame.font",
            "freesansbold.tff",
            "re","sre_compile","sre_parse","sre_constants",
            "Pytower_Defense","Inimigo","Mapa","Componentes","Jogador"]
includefiles = ["Black_Obelisk.png",
                "Explosion snake.png",
                "Little blue snake.png",
                "Little bomb snake.png",
                "Little dead snake.png",
                "Little orange snake.png",
                "Little robot snake.png",
                "Little shell snake.png",
                "Little skull snake.png",
                "wall.png",
                "destrocos.png",
                "grama.jpg",
                "Bone Crushing.wav",
                "Grenade.wav",
                "Hammering.wav",
                "Metal_Drop.wav",
                "Big Bomb.wav",
                "freesansbold.ttf"]
excludes=[]
packages=[]

setup(
     version = "1.0",
     description = "No Description",
     author = "Bruno Iochins Grisci",
     name = "Pytower Defense",
     options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
     executables = [exe]
     )