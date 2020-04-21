import turtle
import winsound
w=turtle.Screen()
w.title("PING PONG")
w.setup(width=1000,height=800)
w.bgcolor("black")
w.tracer(0)
#score
p_a=0
p_b=0
bb=True

#paddle
a=turtle.Turtle()
a.speed(0)
a.shape("square")
a.color("red")
a.shapesize(stretch_len=1,stretch_wid=5)
a.penup()
a.goto(-460,0)

#paddle b
b=turtle.Turtle()
b.speed(0)
b.shape("square")
b.color("Red")
b.shapesize(stretch_wid=5,stretch_len=1)
b.penup()
b.goto(460,0)

#SCORE
p =turtle.Turtle()
p.penup()
p.color("White")
p.hideturtle()
p.goto(0,360)
p.write("player A : 0  player B :0",align="center",font=("courier",20,"normal"))

#ball
c=turtle.Turtle()
c.shape("square")
c.color("white")
c.goto(0,0)
c.penup()
c.dx=1
c.dy=-1

def a_up():
    y=a.ycor()
    y+=25
    a.sety(y)
def a_down():
    y=a.ycor()
    y-=25
    a.sety(y)

def b_up():
    y=b.ycor()
    y+=25
    b.sety(y)
def b_down():
    y=b.ycor()
    y-=25
    b.sety(y)

#listen

w.listen()
w.onkeypress(a_up,"w")
w.onkeypress(a_down,"s")
w.onkeypress(b_up,"Up")
w.onkeypress(b_down,"Down")

while bb:
    w.update()


    c.setx(c.xcor()+ c.dx)
    c.sety(c.ycor()+ c.dy)

    if c.ycor()>390:
        c.sety(390)
        c.dy *= -1
    if c.ycor()<-390:
        c.sety(-390)
        c.dy *=-1

    if c.xcor()>490:
        c.goto(0,0)
        c.dx *= -1
        p_a+=1
        p.clear()
        p.write("player A : {} player B : {}".format(p_a,p_b), align="center", font=("courier", 20, "normal"))
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if c.xcor()<-490:
        c.goto(0,0)
        c.dx *= -1
        p_b+=1
        p.clear()
        p.write("player A : {}  player B : {}".format(p_a,p_b), align="center", font=("courier", 20, "normal"))
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if(c.xcor()>450 and c.xcor()<460) and (c.ycor()<b.ycor()+40 and c.ycor()>b.ycor() - 40):
        c.setx(450)
        c.dx *= -1
    if (c.xcor() < -450 and c.xcor() > -460) and (c.ycor() < a.ycor() + 40 and c.ycor() > a.ycor() - 40):
        c.setx(-450)
        c.dx *= -1

    if p_a ==10 or p_b ==10:
        bb=False

p.goto(0,0)
p.write("GAME OVER!!!",font=("courier",30,"normal"))