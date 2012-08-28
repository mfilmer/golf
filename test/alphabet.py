r=raw_input()
i=ord(r[0])
exec"i+=1-26*(i%%32>25);print chr(i)%s;"%","["."in r:]*26