#!/bin/python
class Konto:
    def __init__(self, saldo, navn):
        self.__saldo=saldo
        self.__navn=navn

    def innskudd(self, inn):
        self.__saldo += inn
    def uttak(self, ut):
        if ut <= self.__saldo:
            self.__saldo -=ut
        else:
            print("nei")
    def get_saldo(self):
        return self.__saldo
    def set_navn(self,nytt):
        self.__navn=str(nytt)
min_konto=Konto(150,"bruks")
print(min_konto.get_saldo)
min_konto.uttak(200)
