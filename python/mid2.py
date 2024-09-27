#!/bin/python
noe = input()
ss=len(noe)-1
i=0
vokal=0
print(ss)
while ss>-1:
    str(noe[i]),str(noe[ss])==noe[ss],noe[i]
    print (noe[ss])
    if noe[ss]=="a" or noe[ss]=="e" or noe[ss]=="i" or noe[ss]=="o" or noe[ss]=="u" or noe[ss]=="y" or noe[ss]=="æ" or noe[ss]=="ø" or noe[ss]=="å":
        vokal=int(vokal)+1   
    i=i+1
    ss=ss-1
print (vokal)
