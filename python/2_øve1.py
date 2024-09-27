#!/bin/python
class Figur:
    klengde=0
    kbrede=klengde
    rlengde=0
    rbrede=0
    radius=0
    kareal=0
    rareal=0
    sareal=0

    def kvadrat(self):
        global klengde
        global kbrede
        klengde=input("kvadrat side")
        kbrede=klengde

    def rektangel(self):
        global rbrede
        global rlengde 
        rlengde=input("rektangel lengde")
        rbrede=input("rektangel brede")
    def sirkel(self):
        global radius
        radius=input("radius til sirkel")
    def areal(self):
      global kareal
      global rareal
      global sareal
      global rbrede
      global rlengde 
      global klengde
      global kbrede
      global radius
      kareal=int(kbrede)*int(klengde)
      rareal=int(rbrede)*int(rlengde)
      sareal=int(radius)*int(radius)
      sareal=int(sareal)*3.14
      print(kareal)
      print(rareal)
      print(sareal)
 
noe=Figur()
noe.rektangel()
noe.kvadrat()
noe.sirkel()
noe.areal()





