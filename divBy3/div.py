#-10/3 = -4
#int(' -'[x<0]+str(len(range(2-(x<0)*2,abs(x),3))))
int(' -'[x<0]+str(len(range([2,0][x<0],abs(x),3))))

#-10/3 = -3
int(' -'[x<0]+str(len(range(2,abs(x),3))))