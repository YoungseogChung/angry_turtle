import turtle
import math

player=turtle.Turtle()
target=turtle.Turtle()  

player.shape("turtle")
screen = player.getscreen()


def turnleft():#왼쪽으로 5도 전환
    player.left(5)

def turnright(): #오른쪽으로 5도 전환
    player.right(5)

def speedup(): # 속도 증가
    global velocity
    velocity=velocity+2

def speeddown(): # 속도 감소
    global velocity
    velocity=velocity-2
    
def fire():
    x=0
    y=0
    angle = player.heading() # 초기각도
    vx = velocity * math.cos(angle *3.14/ 180.0)
    vy = velocity * math.sin(angle *3.14/ 180.0)
    while player.ycor() >= 0:
        vx = vx
        vy = vy-10
        x = x+vx
        y = y+vy
        player.goto(x, y)

velocity = 50 # 초기속도 50픽셀/sec

import turtle as t
import random


d = t.distance(target, 0)
t.sety(random.randint(10, 100))
if d < 25:
    t.color("blue")
    t.write("Good!", False, "center", ("", 15))
else:
        t.color("red")
        t.write("Bad!", False, "center", ("", 15))
        t.color("black")
        t.goto(-200, 10)
        t.setheading(ang)
  
t.goto(-300, 0)
t.down()
t.goto(300, 0)

target = random.randint(100, 150)
t.pensize(3)
t.color("green")
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target +25, 2)



screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(fire, "space")
screen.onkeypress(speedup, "Up")
screen.onkeypress(speeddown, "Down")
screen.listen()
t.mainloop()
