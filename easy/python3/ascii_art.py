#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

myletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

lignes_ascii_en_1bloc = ''
dico_ascii_ligne = {}
ligne_out = []
dico_result = {}

largeur_lettre = int(input()) # Toutes les lettres font la même largeur.
hauteur_lettre = int(input()) # Toutes les lettres font la même hauteur.
ligne_de_texte = str(input()).upper() # texte composée de N caractères ASCII.

new_ligne = ''

for letter in ligne_de_texte :
    if letter in myletters :
        new_ligne += letter
    else :
        new_ligne += '?'

for i in range(hauteur_lettre):
    ligne = input()
    lignes_ascii_en_1bloc += ligne #on a tout ascii en 1bloc

# h ligne
for digit in range(hauteur_lettre) :
    # on découpe lignes_ascii_en_1bloc en plusieurs lignes (h) stocké dans un dico_result
    # sous la forme {'0' : ligne1, '1' : ligne2, '2' : ligne3 ...}
    dico_ascii_ligne[digit] = lignes_ascii_en_1bloc[digit*largeur_lettre*27 : ((digit+1)*largeur_lettre*27)-1]

for letter in new_ligne :
    #on cherche la position où commence la lettre en jeu.
    if letter == '?' :
        position_debut = (26)*largeur_lettre
    else :
        position_debut = (ord(letter)-65)*largeur_lettre

    #on cherche la position où se termine la lettre en jeu.
    position_fin = position_debut+largeur_lettre

    for num in range(hauteur_lettre) :
        # voici la portion sur cette ligne que l'on extrait
        valeur_sur_ligne = (dico_ascii_ligne[num][position_debut:position_fin])

        if num not in dico_result.keys():
                if letter == '?' :
                    dico_result[num] = str(valeur_sur_ligne + ' ')
                else :
                    dico_result[num] = str(valeur_sur_ligne)
        else :
            if letter == '?' :
                dico_result[num] += str(valeur_sur_ligne + ' ')
            else :
                dico_result[num] += str(valeur_sur_ligne)

        # ici on a un dico, avec sur chaque cle, la portion à afficher
        # ex : pour E, on a {0: '### ', 1: '#   ', 2: '##  ', 3: '#   ', 4: '### '}
        # qui donne :
        # + ### +
        # + #   +
        # + ##  +
        # + #   +
        # + ### +

for num in range(hauteur_lettre) :
    ligne_out.append(str(dico_result[num]))

print('\n'.join(map(str, ligne_out)))

# LA LIGNE :

#---------
 #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ###
# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   #
### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ##
# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #
# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #
#-------
