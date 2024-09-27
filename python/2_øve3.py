#!/bin/python
import random
avstand=200000
global vant
vant=0
class Bil:
    global kjørt
    kjørt=0
    def fart():
        global kjørt
        ting=random.randint(1, 6)
        kjørt=kjørt+1+ting
        if kjørt>=avstand:
            global vant
            print("bil vant")
            vant=1
class Motorsykel:
    global mkjørt
    global boost
    boost=random.randint(1, 6)
    mkjørt=2
    def fart():
        global mkjørt
        ting=random.randint(1, 6)
        mkjørt=mkjørt+ting
        if boost > 4:
            mkjørt=mkjørt+10
        if mkjørt>=avstand:
            global vant
            print("motorsykel vant")
            vant=1
class Fly:
    global fkjørt
    fkjørt=0
    def fart():
        global fkjørt
        ting=random.randint(3, 12)
        fkjørt=fkjørt+ting-3
        if fkjørt>=avstand:
            global vant
            print("fly vant")
            vant=1

b=Bil
m=Motorsykel
f=Fly

while vant < 1 :
    print(f"{kjørt} bil")
    print(f"{mkjørt} motor")
    print(f"{fkjørt} Fly")
    f.fart()
    b.fart()
    m.fart()

