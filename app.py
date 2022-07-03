from turtle import *
from constants import *
from math import sqrt
from random import random

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
speed(0) # set speed to 0 and only set the delay
if dot_amount > 10_000:
	if dot_amount < 50_000:
		tracer(1000)
	elif dot_amount < 100_000:
		tracer(5000)
	elif dot_amount < 500_000:
		tracer(10_000)
	elif dot_amount > 999_999:
		tracer(50_000)
delay(dot_generation_speed)

dots_in_circle = 0
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

	# do not print dots if they are out of range
	if only_show_dot_in_range == False or between(range_to_zero, only_show_dot_in_range):
		goto(rand_x, rand_y)
		down()
		small_dot()
		if show_dot_range:
			write(int(range_to_zero), font=("Arial", dot_range_font_size, "normal"))
		up()

	calc_pi = round(4 * dots_in_circle / i, 5)
	log(f"Current calculated value of pi: {calc_pi}")

	if show_calculated_pi and (i == dot_amount or i % update_pi_text_interval_size == 0):
		# remove the text from the window
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
		if i == dot_amount:
			string = f"Calculation Completed! \n Finally calculated PI is: {calc_pi} | Generated dots: {i}"
		else:
			string = f"Calculated PI is: {calc_pi} | Generated dots: {i}"
		write(string, font=("Arial", 10, "normal"))
		up()

### don't close window automatically
done()
