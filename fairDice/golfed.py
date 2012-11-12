import randomizer

#serious and working
R = randomizer.Unfair()
i=7
while i>5:[R.random()for x in range(9)];i=int(`R.random()`[-1])
print i+1

exit()
#serious and non working(replace unfair random function calls)
#63
i=7
while i>5:[R()for x in range(9)];i=int(`R()`[-1])
print i+1


#non-serious (against the rules anyway)
#for x in'11111':getRandom()     #17 (counting newline)
#print getRandom()               #6
