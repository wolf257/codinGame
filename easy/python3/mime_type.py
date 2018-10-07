#!/usr/bin/env python3
#-*- coding : utf8 -*-

import sys
import math

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
dico = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    dico[ext.lower()]=mt

for i in range(q):
    fname = input()  # One file name per line.
    if not "." in fname:
        print("UNKNOWN")
        continue

    fext = fname.split(".")[-1].lower()

    if fext in (dico.keys()) :
        print(dico[fext])
    else:
        print('UNKNOWN')
