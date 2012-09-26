d 0(a:r)=r;d n(a:r)=a:d(n-1)r
t[]=1;t(f:r)=sum[(-1)^j*f!!j*t(map(d j)r)|j<-[0..length f-1]]
main=interact$show.t.map(map read.words).lines