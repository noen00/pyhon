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
        self.lyd=lyd
        super().lag_lyd(self,"noe")
    def cat(self):
        print(f"{self.navn} lol")
hund1=Hund("Fido")
hund1.lag_lyd("lag")
hund1.logre()
cat1=Katt("aa")
cat1.lag_lyd()