from turtle import *
from constants import *
from math import sqrt, ceil
from random import random
from time import time
from datetime import datetime

def angle(angle):
	setheading(angle)

def small_dot():
	dot(dot_size)

def log(information):
	if show_debug_information:
		print(information)

def between(value, min_max_tuple):
	return min_max_tuple[0] <= value <= min_max_tuple[1]

### calculate other constants
max_x = 100
max_y = 100
end_x = (max_x, 0)
end_y = (0, max_y)
end_coordinate_system = (max_x, max_y)
zero_point = (0, 0) # coordinate origin

### setup default options
setup(700, 700)
bgcolor(bg_color)
setworldcoordinates(-10, -10, 110, 110)
delay(10)
color(draw_color)
fillcolor(draw_color)
speed(draw_speed)
width(line_width)
hideturtle()
up() # on start hide turtle and the pen

### draw the coordinate system

# draw the x-axis
goto(zero_point)
angle(0)
down()
forward(100)

# draw the arrow
position1 = pos()
angle(160)
forward(arrow_length)
up()
goto(position1)
down()
angle(200)
forward(arrow_length)
del position1
up()

# draw the y-axis
goto(zero_point)
angle(90)
down()
forward(100)

# draw the arrow
position1 = pos()
angle(290)
forward(arrow_length)
up()
goto(position1)
down()
angle(250)
forward(arrow_length)
del position1
up()

### draw the end/border of the system
if show_coordinate_system_border:
	goto(end_x)
	color(coordinate_system_border_color)
	down()
	goto(end_coordinate_system)
	goto(end_y)
	up()
	color(draw_color)
up()

### draw the quarter circle
if show_quarter_circle:
	goto(end_x)
	down()
	angle(90)
	circle(100, 90, 180) # first param is radius, second param is extent and the last are the steps (accuracy)
	up()

###  add random dots
speed(0)
delay(dot_generation_speed)
tracer(dot_print_tracer)

start_time = time()
dot_interval = int(ceil(dot_amount / max_visible_dots)) # only show the xth dot
dots_in_circle = 0
dots_in_window_visible = 0
for i in range(1, dot_amount + 1):
	rand_x = random() * 100
	rand_y = random() * 100
	log(f"Coordinates of new dot -> (x: {rand_x} | y: {rand_y})")

	range_to_zero = sqrt(pow(rand_x, 2) + pow(rand_y,2))
	if not range_to_zero > 100:
		color(dot_inside_color)
		dots_in_circle += 1
	else:
		color(dot_outside_color)

	# do not print dots if they are out of interval
	if (i - 1) % dot_interval == 0:
		goto(rand_x, rand_y)
		down()
		small_dot()
		if show_dot_range:
			write(int(range_to_zero), font=("Arial", dot_range_font_size, "normal"))
		up()
		dots_in_window_visible += 1

	calc_pi = round(4 * dots_in_circle / i, 5)

	if i % log_pi_every_x_iteration == 0:
		ct = datetime.now()
		print(f"{ct.hour}:{ct.minute}:{ct.second}: Current calculated value of pi: {calc_pi} | Generated dots: {i} | Visible dots: {dots_in_window_visible}")

	if i == dot_amount:
		# clear area
		color(bg_color)
		fillcolor(bg_color)
		goto(0, -3)
		angle(0)
		begin_fill()
		down()
		forward(100) # go to the right
		right(90)
		forward(4) # to downwards
		right(90)
		forward(100) # go to the left
		right(90)
		forward(4) # go upwards
		end_fill()
		up()

		# render calculated pi on window
		color(draw_color)
		goto(2, -6)
		down()

		execution_time = time() - start_time
		success_message = f"---------- \nCalculation Completed! \nFinally calculated PI is: {calc_pi} | Generated dots: {i} | Execution time: {execution_time}s"
		print(success_message)
		write(
			success_message,
			font=("Arial", 10, "normal")
		)
		up()
		update() # force printing the new PI-Calculation to the screen

### don't close window automatically
done()
