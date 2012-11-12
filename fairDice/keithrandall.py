from random import randint
n=0
def r():
    global n;n+=1
    return randint(1,n)

D=lambda:eval('r(),'*6)[-1]%6+1

with open('randall.txt','w') as f:
    for i in range(10000):
        f.write('{0}\n'.format(D()))