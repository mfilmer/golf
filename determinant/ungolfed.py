def det(x):
    l = len(x)
    if l == 1:
        return x[0][0]
    return sum([(-1)**i*x[i][0]*det(minor(x,i+1,1)) for i in range(l)])

def minor(x,i,j):
    y = x[:]
    del(y[i-1])
    y=zip(*y)
    del(y[j-1])
    return zip(*y)

def main():
    x = [input()]
    for i in range(len(x[0])-1):
        x += [input()]
    print det(x)

if __name__ == '__main__':
    main()
    x = [[1,-4,9],[-6,7,3],[1,2,3]]
