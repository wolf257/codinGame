#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

myletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

new_ligne, lignes_ascii_en_1bloc = '', ''
dico_ascii_ligne, dico_result = {}, {}

l = int(input()) # Toutes les lettres font la même largeur.
h = int(input()) # Toutes les lettres font la même hauteur.
ligne_de_texte = str(input()).upper() # texte composée de N caractères ASCII.

new_ligne += ''.join([letter if letter in myletters else '?' for letter in ligne_de_texte])

lignes_ascii_en_1bloc += ''.join([input() for i in range(h)])

for digit in range(h) :
    # on découpe lignes_ascii_en_1bloc en plusieurs lignes (h) stocké dans un dico_result
    # sous la forme {'0' : ligne1, '1' : ligne2, '2' : ligne3 ...}
    dico_ascii_ligne[digit] = lignes_ascii_en_1bloc[digit*l*27 : ((digit+1)*l*27)-1]

for letter in new_ligne :
    position_debut = 26*l if letter == '?' else (ord(letter)-65)*l
    position_fin = position_debut+l

    for num in range(h) :
        # voici la portion sur cette ligne que l'on extrait
        valeur_sur_ligne = (dico_ascii_ligne[num][position_debut:position_fin])

        if num not in dico_result.keys():
            dico_result[num] = str(valeur_sur_ligne + ' ') if letter == '?' else str(valeur_sur_ligne)
        else :
            dico_result[num] += str(valeur_sur_ligne + ' ') if letter == '?' else str(valeur_sur_ligne)

print('\n'.join(map(str, [str(dico_result[num]) for num in range(h)])))

# LA LIGNE :

#---------
 #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ###
# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   #
### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ##
# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #
# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #
#-------
