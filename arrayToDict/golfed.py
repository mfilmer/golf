{x[0]:sum([y[1]for y in a if y[0]==x[0]])for x in a}

#with unpacking and removed brackets
{X:sum(y for Y,y in a if Y==X)for X,x in a}