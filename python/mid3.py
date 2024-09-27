#!/bin/python
ting=0
nooo=0

noe = input("skriv tall")

def nnn():
    global nooo
    global noe
    global ting
    if int(nooo) < int(noe):
        nooo=noe

ting=int(noe)+ting
nnn()
noe = input("skriv tall")
ting=int(noe)+ting
noe = input("skriv tall")
ting=int(noe)+ting
nnn()
noe = input("skriv tall")
ting=int(noe)+ting
nnn()
print (ting)
print (nooo)

