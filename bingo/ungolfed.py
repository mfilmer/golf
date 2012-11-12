
B = [raw_input().split() for i in range(5)]
B = [[0 if x == '*' else x for x in row] for row in B]

while True:
    tCall = raw_input()
    print tCall
    call = tCall[1:]
    B = [[0 if x == call else x for x in row] for row in B]
    if not all(map(any,B)) or not all(map(any,zip(*B))):
        print 'BINGO!'
        break
    F = reduce(lambda x,y:x+y,B)
    F = B[0]+B[1]+B[2]+B[3]+B[4]
    F=[]
    for i in range(5):F+=B[i]
    if not any(F[::6]) or not any(F[4:24:4]):
        print 'BINGO!'
        break
