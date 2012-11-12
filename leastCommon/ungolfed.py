from collections import*
a=Counter().most_common()[-10:]
a.reverse()
for b in a:print b[0]+':',`n(b[1])`.rjust(len(`a[0][0]`))