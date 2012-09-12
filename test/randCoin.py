import random
whichTest = True    #True -> python's random
                    #False -> coin flip random

outputFileName = 'porOutput.txt' if whichTest else 'testOutput.txt'

with open(outputFileName,'w') as f:
    x = 0.0
    inc = 0.01
    f.write('desired probability, true count, false count, actual probability\n')
    while x < 1:
        tCount = 0
        fCount = 0
        for count in xrange(100000):
            if whichTest:
                rand = random.random() < x
            else:
                rand = sum(random.randint(0,1)*2**-i for i in range(9))<x*2
            if rand:
                tCount += 1
            else:
                fCount += 1

        probability = float(tCount)/(fCount+tCount)
        out = '{0}, {1}, {2}, {3}'.format(x,tCount,fCount,probability)
        f.write(out + '\n')
        print out
        x += inc