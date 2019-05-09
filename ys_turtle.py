import turtle, math, random


player = turtle.Turtle()
player.shape("turtle")
screen = player.getscreen()
targets = []

def turnleft():
	player.left(5)				# 왼쪽으로 5도 회전

def turnright():
	player.right(5)				# 오른쪽으로 5도 회전

def spawn_target():
	temp_t = turtle.Turtle()
	temp_t.color("red")
	temp_t.shape("circle")
	temp_t.penup()
	temp_t.speed(0)
	x_pos = random.randint(-20, 20)
	y_pos = random.randint(0, 20)
	temp_t.goto(x_pos, y_pos)
	targets.append((temp_t, x_pos, y_pos))

def fire():
	prev_x, x = 0, 0
	prev_y, y = 0, 0
	global vel
	velocity = vel				# 초기 속도 50픽셀/sec
	angle = player.heading()		# 초기 각도
	vx = velocity * math.cos(angle * 3.14 / 180.0)	# 도 -> 라디안
	vy = velocity * math.sin(angle * 3.14 / 180.0)	# 도 -> 라디안
	while player.ycor() >= 0 :		# y좌표가 음수가 될 때까지
		vx = vx
		vy = vy - 10
		prev_x = x
		prev_y = y
		x = x + vx
		y = y + vy
		player.goto(x, y)
		print(x,y)
		print(player.xcor(), player.ycor())
		for target in targets:
			target_t = target[0]
			target_x = target[1]
			target_y = target[2]
			print(target_x, target_y)
			if ((prev_x<target_x and target_x<x)or(prev_x>target_x and target_x>x)) \
			and ((prev_y<target_y and target_y<y)or(prev_y>target_y and target_y>y)):
				print('here')
				target_t.write('YOU GOT ME! :(')
				target_t.hideturtle()

			# if ((target_x-2)<x) and ((target_x+2)>x) and \
			#    ((target_y-2)<y) and ((target_y+2)>y):
			#    print('here')
			#    target_t.clear()

spawn_target()
vel = float(turtle.textinput('Velocity', 'Set Velocity'))
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(fire, "space")		# 사용자가 스페이스키를 누르면
screen.listen()

turtle.done()
