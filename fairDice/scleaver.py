from random import randint
n=0
def r(z):
    global n;n+=1
    return randint(1,n)

import math;d=lambda:math.ceil(6.*r(r(r(r(r(r(0))))))/n)

with open('scleaverTest.txt','w') as f:
    for i in range(100000):
        f.write('{0}\n'.format(d()))