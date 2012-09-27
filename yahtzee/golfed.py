#389
# def D():return M(int,raw_input().split())
# def F(d):d=sorted(set(d));return[d[x+1]-d[x]for x in R(len(d)-1)]
# S=sum;M=map;R=range;s=S(x for i in R(6)for x in D()if x==i+1)
# for i in R(2):d=D();s+=[0,S(d)][max(M(d.count,d))>2+i]
# d=D();a=M(d.count,d);s+=[0,25][2in a and 3in a or 5in a]
# for i in R(2):s+=[0,30+i*10]['1, 1, 1'+', 1'*i in`F(D())`]
# d=D();s+=[0,50][d.count(d[0])==5]
# print s+S(D())

#301/363
S=sum;R=range;D=[map(int,raw_input().split())for i in R(13)];s=S(x for i in R(6)for x in D[i]if x==i+1)
for i in R(2):d=D[6+i];s+=[0,S(d)][max(map(d.count,d))>2+i];d=sorted(set(D[9+i]));s+=[0,30+i*10]['1, 1, 1'+', 1'*i in`[d[x+1]-d[x]for x in R(len(d)-1)]`]
e=D[8];a=map(e.count,e);d=D[11];print s+S(D[12])+[0,50][d.count(d[0])>4]+[0,25][2in a and 3in a or 5in a]
