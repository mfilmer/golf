from itertools import*
def f(a):return [x for x in permutations(a) if x==tuple(sorted(a))][0]