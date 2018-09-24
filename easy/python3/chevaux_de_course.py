#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input()) #nbre chevaux
liste_valeurs = []
liste_classee = []
liste_ecarts = []

for i in range(n):
    pi = int(input())

    liste_valeurs.append(pi)

liste_classee = liste_valeurs.copy()
liste_classee.sort()

#calcul des écarts
for i in range(n-1):
    ecart = abs(liste_classee[i] - liste_classee[i+1])
    liste_ecarts.append(ecart)

ecart_min = min(liste_ecarts)


print(ecart_min)
