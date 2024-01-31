from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
screen.listen()


def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def clockwise():
    tim.right(10)

def anti_clock():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkeyrelease(key="s",fun=backward)
screen.onkeyrelease(key="w",fun=forward)
screen.onkeyrelease(key="a",fun=anti_clock)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clear)


screen.exitonclick()