#!/bin/python
class Dyr:
    def __init__( self,navn):
        self.navn=navn
    def lag_lyd(self, lyd):
        print(f"{self.navn} {self.lyd}")
class Hund(Dyr):
    def lag_lyd(self, lyd):
        super().lag_lyd("bbbb")
    def logre(self):
        print(f"{self.navn} lol")
class Katt(Dyr):
    def lag_lyd(self, lyd):
        super().lag_lyd("noe")
hund1=Hund("Fido")
hund1.lag_lyd
hund1.logre()
cat1=Katt("aa")
cat1.lag_lyd()