### setup constants
# performance
dot_amount = 100_000                      # amount of dots that will be generated
max_visible_dots = 1500                       # number of dots that are maximal displayed
draw_speed = 8                              # speed to draw the complete coordinate system, 1: slowest, 6: normal, 10: fast, 0: fastest
dot_generation_speed = 0                    # number between 0 and ~50, the higher the value, the slower the program
log_pi_every_x_iteration = 10_000           # every x iteration the calculated-pi is printed to the console
dot_print_tracer = 10                        # 1 = render each "object" to the window, x = render after x draws the objects to the window (the higher, the faster)

# visibility
show_debug_information = False              # show debug logs
show_quarter_circle = True                  # render the quarter circle
show_calculated_pi = True                   # render the calculated pi
show_dot_range = True                       # print the range next to the dot
show_coordinate_system_border = True        # show the border of the coordinate system

# color / design
dot_size = 4                                # size of a dot
arrow_length = 3                            # length of the coordinate system arrows in pixel, 0 = hide
line_width = 1                              # width of the coordinate system lines
dot_range_font_size = 7                     # font size of the dot range text
bg_color = "#ffffff"                        # select background color by name ("white", "red") or by hex-code
draw_color = "#000000"                      # color of the coordinate system
dot_outside_color = "#ff0000"               # color of the dots that are outside the radius
dot_inside_color = "#00961c"                # color of the dots that are inside the radius
coordinate_system_border_color = "#e0dede"  # color of the coordinate system border

