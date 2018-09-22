#!/usr/bin/env python3
#-*- coding : utf8 -*-

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse

temp_courante = input()

value_to_print = None

if len(temp_courante) == 0 :
    value_to_print = 0
else :
    listTemp = temp_courante.split()
    value_to_print = listTemp[0]

    for temperature in listTemp :
        if (abs(int(temperature))) < abs (int(value_to_print)) :
            value_to_print = temperature
        elif abs(int(temperature)) == abs(int(value_to_print)) :
            value_to_print = max(temperature, value_to_print)

print(value_to_print)
