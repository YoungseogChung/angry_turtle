import turtle, math, random
import tkinter.messagebox

player = turtle.Turtle()
player.shape("turtle")
screen = player.getscreen()
spawn_range = 0
targets = []
dead_targets = []
vel = 0

def turnleft():
	player.left(5)				

def turnright():
	player.right(5)				

def set_difficulty():

	set_diff_msg = 'Set difficulty: Easy, Medium, Hard'
	diff_setting = ''
	while (len(diff_setting)<1) or (diff_setting[0] not in ['e','E','m','M','h','H']):
		diff_setting = turtle.textinput('Game Difficulty', set_diff_msg)
		set_diff_msg = 'Answer Must be Easy, Medium or Hard'
	
	global spawn_range
	if diff_setting[0] in ['e','E']:
		spawn_range=100
	elif diff_setting[0] in ['m','M']:
		spawn_range=200
	elif diff_setting[0] in ['h','H']:
		spawn_range=300	
	


def set_num_targets():
	num_targets = 0
	targets_msg = 'Set Number of Targets'
	while num_targets < 1:
		num_targets = int(turtle.textinput('Number of Targets', targets_msg))
		if (num_targets<1):
			targets_msg = 'Number of Targets Must be Greater Than 1'
	
	for _ in range(num_targets): spawn_target()

def spawn_target():
	temp_t = turtle.Turtle()
	temp_t.color("red")
	temp_t.shape("circle")
	temp_t.penup()
	temp_t.speed(0)
	
	global spawn_range
	x_pos = random.randint(-spawn_range, spawn_range)
	y_pos = random.randint(30, spawn_range)
	temp_t.goto(x_pos, y_pos)
	targets.append((temp_t, x_pos, y_pos))

def clean_dead_targets():
	global dead_targets
	for dead_t in dead_targets:
		dead_t.clear()
	dead_targets = []	

def stop():
    answer = tkinter.messagebox.askyesno('Game Complete!', "Play again?")
    if answer:
        main()
    else:
        turtle.bye()

def reposition_player():
	player.penup()
	player.goto(0,0)
	player.pendown()
	player.clear()
	
	global vel
	vel_input = ''
	vel_msg = 'Set Velocity'
	while (len(vel_input)<1) or (not vel_input.isnumeric()):
		vel_input = turtle.textinput('Velocity', vel_msg)
		vel_msg = 'Velocity must be a number'
	vel = float(vel_input) 	
	screen.listen()

def fire():
	prev_x, x = 0, 0
	prev_y, y = 0, 0
	
	player.goto(x,y)
	global vel
	velocity = vel				
	angle = player.heading()		
	vx = velocity * math.cos(angle * 3.14 / 180.0)	
	vy = velocity * math.sin(angle * 3.14 / 180.0)	
	while player.ycor() >= 0 :		
		vx = vx
		vy = vy - 10
		prev_x = x
		prev_y = y
		x = x + vx
		y = y + vy
		player.goto(x, y)
		for target in targets:
			target_t = target[0]
			target_x = target[1]
			target_y = target[2]
			# check if any targets hit
			if ((prev_x-10<target_x and target_x<x+10)or(prev_x+10>target_x and target_x>x-10)) \
			and ((prev_y-10<target_y and target_y<y+10)or(prev_y-10>target_y and target_y>y+10)):
				target_t.write('YOU GOT ME! :(')
				dead_targets.append(target_t)
				target_t.hideturtle()
				targets.remove(target)
	if len(targets)==0:
		# cleared all targets, ask if play again
		stop()		
	else:
		# have targets left, ask if continue playing
		cont_game_msg = 'Continue Playing Game?\n Answer Yes or No'
		cont_game = ''
		while (len(cont_game)<1) or (cont_game[0] not in ['y', 'Y', 'n', 'N']):
			cont_game = turtle.textinput('Continue Game', cont_game_msg)
			cont_game_msg = 'Answer Must be Yes or No'
		if cont_game[0] in ['y','Y']:
			clean_dead_targets()
			reposition_player()
		elif cont_game[0] in ['n','N']:
			turtle.bye()
		
	
def main():
	set_difficulty()
	clean_dead_targets()
	set_num_targets()
	reposition_player()
	screen.onkeypress(turnleft, "Left")
	screen.onkeypress(turnright, "Right")
	screen.onkeypress(fire, "space")	
	screen.listen()
main()
turtle.done()
