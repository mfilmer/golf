#!/usr/bin/env python

from curses import*
M=0xf3e499e601c0d0240b0380679927cf;S=initscr();S.keypad(1);x,y=2,2;A=S.addstr;[A(a,b,[' ','#'][M>>(10*a+b)&1]) for a in range(12) for b in range(10)]
while 1:A(y,x,'@');k=S.getch();A(y,x,' ');X=[[x,x-1],[x+1,1]][k==261][k==260];Y=[[y,y-1],[y+1,y+1]][k==258][k==259];x,y=[(X,Y),(x,y)][M>>(10*Y+X)&1]
