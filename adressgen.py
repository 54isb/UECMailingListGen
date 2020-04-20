# -*- coding: utf-8 -*-
import csv
import subprocess
from pykakasi import kakasi
import pprint

cmd = "nkf -u RSMeiboCsv.csv > utf.csv"
subprocess.call(cmd, shell=True)

with open('./utf.csv', encoding="UTF-8") as f:
    reader = csv.reader(f)
    l = [row for row in reader]

l=l[4:] #eliminate a header
l_T = [list(x) for x in zip(*l)] #transpose

pin = l_T[1] #get student PINs
name = l_T[3] #get student names

#generate roman name
kakasi = kakasi()
kakasi.setMode('K', 'a')
conv = kakasi.getConverter()
alphabet_name = list(map(conv.do,name))

#generate email addresses
for ix,val in enumerate(alphabet_name):
    print(val[0]+pin[ix]+"@edu.cc.uec.ac.jp, ", end='')

print()

cmd = "rm utf.csv"
subprocess.call(cmd, shell=True)
