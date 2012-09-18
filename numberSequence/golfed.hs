--putStrLn$take x("0"++(cycle"42"))
--putStrLn$take x(cycle"02")
--putStrLn$take x$cycle"02"

a 4=[3,1,4,2]
a x=let b=filter even[1..x]++filter odd[1..x]in tail b++[b!!0]