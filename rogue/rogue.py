#!/usr/bin/env python

from curses import*
M=0xf3e499e601c0d0240b0380679927cf;S=initscr();S.keypad(True);x,y=2,2;A=S.addstr;[A(a,b,[' ','#'][M>>(10*a+b)&1]) for a in range(12) for b in range(10)]
while 1:A(y,x,'@');k=S.getch();A(y,x,' ');X=x+1 if k==261 else x-1 if k==260 else x;Y=y+1 if k==258 else y-1 if k==259 else y;x,y=(x,y)if M>>(10*Y+X)&1 else(X,Y)
