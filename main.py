import turtle

system_window = turtle.Screen()
system_window.title("Go Game")
system_window.bgcolor("black")
system_window.setup(width=800, height=400)

# madrab1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape('square')
madrab1.goto(-370.0, 0.0)
madrab1.penup()
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5, stretch_len=1)

# madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape('square')
madrab2.goto(370.0, 0.0)
madrab2.penup()
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.goto(0.0, 0.0)
ball.penup()
ball.color("white")
ball.dx = 8
ball.dy = -8


# functions
def madrab1_up():
    y = madrab1.ycor();
    madrab1.sety(y + 20)


def madrab1_down():
    y = madrab1.ycor();
    madrab1.sety(y - 20)


def madrab2_up():
    y = madrab2.ycor();
    madrab2.sety(y + 20)


def madrab2_down():
    y = madrab2.ycor();
    madrab2.sety(y - 20)


# keyboard binding
system_window.listen()
system_window.onkeypress(madrab1_up, 'w')
system_window.onkeypress(madrab1_down, 's')
system_window.onkeypress(madrab2_up, 'Up')
system_window.onkeypress(madrab2_down, 'Down')

while True:
    system_window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() >= 180:
        ball.sety(180)
        ball.dy *= -1

    if ball.ycor() < -180:
        ball.sety(-180)
        ball.dy *= -1

    if ball.xcor() > 400:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.dx *= -1

    if ( ball.xcor() > 360 and ball.xcor() < 370 ) and (ball.ycor() < madrab2.ycor()+40 and ball.ycor() > madrab2.ycor()-40):
        ball.setx(360)
        ball.dx *= -1
    #
    if ( ball.xcor() < -360 and ball.xcor() > -370 ) and (ball.ycor() < madrab1.ycor()+40 and ball.ycor() > madrab1.ycor()-40):
        ball.setx(-360)
        ball.dx *= -1
