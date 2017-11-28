#def#
import turtle
import math
def sin(x):
    y=math.sin(x)
    return y
def cos(x):
    y=math.cos(x)
    return y

#solar system#
wn=turtle.Screen()
wn.bgcolor("black")
Sun=turtle.Turtle()
Mercury=turtle.Turtle()
Earth=turtle.Turtle()
Marz=turtle.Turtle()
Saturn=turtle.Turtle()
Jupiter=turtle.Turtle()
Uranus=turtle.Turtle()
star=[Mercury,Earth,Marz,Saturn,Jupiter,Uranus]

#color#
Sun.color("red")
Mercury.color("white")
Earth.color("blue")
Marz.color("brown")
Saturn.color("gold")
Jupiter.color("orange")
Uranus.color("skyblue")

#shape#
Sun.shape("circle")
for i in range (6):
    star[i].shape("circle")

#pensize,shapesize#
Sun.pensize(4)
for i in range (6):
    star[i].pensize(1)

Sun.shapesize(4)
Mercury.shapesize(0.3)
Earth.shapesize(1)
Marz.shapesize(0.6)
Saturn.shapesize(2.7)
Jupiter.shapesize(2.5)
Uranus.shapesize(2)

#starting point#
sp1=0
sp2=5
sp3=20
sp4=68
sp5=85
sp6=210

#penup#
Mercury.pu()
Earth.pu()
Marz.pu()
Saturn.pu()
Jupiter.pu()
Uranus.pu()

Mercury.setpos(72*cos(sp1)-17,74.5*sin(sp1))
Earth.setpos(101*cos(sp2)-30,100*sin(sp2))
Marz.setpos(200*cos(sp3)-50,202*sin(sp3))
Saturn.setpos(250*cos(sp4)-60,255*sin(sp4))
Jupiter.setpos(350*cos(sp5)-70,360*sin(sp5))
Uranus.setpos(430*cos(sp6)-82,438*sin(sp6))

#pendown#
Mercury.pd()
Earth.pd()
Marz.pd()
Saturn.pd()
Jupiter.pd()
Uranus.pd()

#draw orbit#
for i in range(60000):
    star[0].setpos(72*cos(sp1)-17,74.5*sin(sp1))
    sp1=sp1+1/58.6
    star[1].setpos(101*cos(sp2)-30,100*sin(sp2))
    sp2=sp2+1/365
    star[2].setpos(200*cos(sp3)-50,202*sin(sp3))
    sp3=sp3+1/687*2
    star[3].setpos(250*cos(sp4)-60,255*sin(sp4))
    sp4=sp4+1/10760*20
    star[4].setpos(350*cos(sp5)-70,360*sin(sp5))
    sp5=sp5+1/4332*10
    star[5].setpos(430*cos(sp6)-82,438*sin(sp6))
    sp6=sp6+1/30685*30