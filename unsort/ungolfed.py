R=range
def S(L):
 for i in R(len(L)-1):
	if L[i]>L[i+1]:L[i:i+2]=[L[i+1],L[i]];S(L)
a=map(input,['']*100);S(a)
for i in R(100):print a[i/2+i%2*50]

# s=sorted(int(raw_input())for i in range(100))
# for i in range(100):print s[(4*i+4*i/n)%n]