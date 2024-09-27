#!/bin/python
import random
global exp
global lv
global explv
global expa
global expa2
count=0
expa2=3
expa=1
explv=10
lv=1
exp=0
def expgain():
    global exp
    global lv
    global explv
    global expa
    global expa2
    noe=random.randint(expa, expa2)
    exp=exp+noe
    print(f"gained {noe} exp du har nå {exp} exp")
    if exp >= explv:
        exp=exp-explv
        lv=lv+1
        print(f"du har levlet op du er nå på level {lv}")
        explv=explv*1.2
        expa =expa+40
        expa2 =expa2 +40
while lv< 1000:
    count=count+1
    expgain()
print(count)
