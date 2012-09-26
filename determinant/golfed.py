def d(x):
 l=len(x)
 if l<2:return x[0][0]
 return sum([(-1)**i*x[i][0]*d(m(x,i))for i in range(l)])
def m(x,i):y=x[:];del(y[i]);y=zip(*y);del(y[0]);return zip(*y)
def main(): #for unit testing purposes, remove this function when deploying
    x=[input()]
    for i in (len(x[0])-1)*[1]:x+=[input()]
    print d(x)

if __name__ == '__main__':
    main()

#from golfed import *
#x = [[1,-4,9],[-6,7,3],[1,2,3]]     #-240
#y = [[1,-4,9,4],[-6,7,3,7],[1,2,3,-4],[8,4,76,5]]   #-3040
#d(x)
#d(y)
