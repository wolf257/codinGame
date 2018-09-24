#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

posX , posY = initial_tx , initial_ty

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    direction_x = ""
    direction_y = ""

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    if light_x > posX :
        direction_x = "E"
        posX += 1
    elif light_x < posX :
        direction_x = "W"
        posX -= 1

    if (light_y > posY) :
        direction_y = "S"
        posY += 1
    elif (light_y < posY) :
        direction_y = "N"
        posY -= 1

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(direction_y + direction_x)
