#!/bin/python
print("test")
navn = "kjetil"
print(f"test, {navn}")
noe=3
a=1
teas=input()
sss = [5,3,4,6,7,1,"tall",2]
print(a+noe)
print("test", str(a))
print(sss[0:7])
while a < int(teas):
    a=a+1
print(a)


for sss in range(3,7):
    if sss ==5: 
        continue
    print(sss)

def nooe(ting = "noe"):
    print(ting)

nooe("sss")
