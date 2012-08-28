def a(n):return[' 'for n in range(n)]if n in '0123' else n

b=['####\n#2#\n#2#\n#2#\n####','1##1\n2#1\n2#1\n2#1\n1###','####\n#2#\n2#1\n1#2\n####','####\n3#\n1###\n3#\n####']

print map(a,b[0])