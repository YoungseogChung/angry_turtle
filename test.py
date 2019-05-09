import turtle
import random
import math

player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)
screen = player.getscreen()

a1 = turtle.Turtle()
a1.color("red")
a1.shape("circle")
a1.penup()
a1.speed(0)
a1.goto(random.randint(-300, 300), random.randint(-300, 300))

a2 = turtle.Turtle()
a2.color("red")
a2.shape("circle")
a2.penup()
a2.speed(0)
a2.goto(random.randint(-300, 300), random.randint(-300, 300))

def turnleft():
	player.left(30) # 왼쪽으로 30도 회전한다.

def turnright():
	player.right(30) # 오른쪽으로 30도 회전한다.

def play():
	player.forward(2) # 2픽셀 전진
	a1.forward(2)
	a2.forward(2)
	screen.ontimer(play, 10) # 10ms가 지나면 play()를 다시 호출

screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.listen()

turtle.done()



# screen.ontimer(play, 10)
