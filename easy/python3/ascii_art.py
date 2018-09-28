#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, math

l = int(input()) # Toutes les lettres font la même largeur.
h = int(input()) # Toutes les lettres font la même hauteur.
toPrint = input() # texte composée de N caractères ASCII.

ascii_art_lines = [input() for line_to_save in range(h)]

for line_to_output in range(h) :
    for letter in toPrint :
        code_car = (ord(letter.upper())-65) if letter.isalpha() else 26
        print(ascii_art_lines[line_to_output][(l*code_car):(l*(code_car+1))] , end='')
    print()
