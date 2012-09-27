x <- as.matrix(read.table("http://pastebin.com/raw.php?i=ZRMC9B4x"))
S=sum;
P=prod;
T=function(i)table(x[i,]);
Z=function(p,i)grepl(p,do.call(paste0,as.list(diff(sort(unique(x[i,]))))))
S((x[1:6,]==(R=row(x[1:6,])))*R)+ # Upper section
S(x[7,])*any(T(7)>2)+             # 3 of a kind
S(x[8,])*any(T(8)>3)+             # 4 of a kind
25*(P(T(9))%in%5:6)+              # Full house
30*Z("111",10)+                   # Small straight
40*Z("1111",11)+                  # Large straight
50*(P(T(12))==5)+                 # Yahtzee
S(x[13,])                         # Chance