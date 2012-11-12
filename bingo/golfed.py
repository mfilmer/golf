R=raw_input;A=any;F=B=[[[x,0][x=='*']for x in row]for row in[R().split()for i in'11111']]
while all([all(map(A,B)),all(map(A,zip(*B))),A(F[::6]),A(F[4:24:4])]):c=R();print c;C=c[1:];B=[[[x,0][x==C]for x in row]for row in B];F=sum(B,[])
print'BINGO!'