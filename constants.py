### setup constants

arrow_length = 3                            # length of the coordinate system arrows in pixel, 0 = hide
draw_speed = 0                              # speed to draw the complete coordinate system, 1: slowest, 6: normal, 10: fast, 0: fastest
dot_generation_speed = 5                    # number between 0 and ~50
line_width = 1                              # width of the coordinate system lines
bg_color = "#ffffff"                        # select background color by name ("white", "red") or by hex-code
draw_color = "#000000"                      # color of the coordinate system
dot_outside_color = "#ff0000"               # color of the dots that are outside the radius
dot_inside_color = "#00961c"                # color of the dots that are inside the radius
show_coordinate_system_border = True        # show the border of the coordinate system
coordinate_system_border_color = "#e0dede"  # color of the coordinate system border
show_dot_range = True                       # print the range next to the dot
only_show_dot_in_range = False              # False or tuple with (min_value, max_value)
dot_range_font_size = 7                     # font size of the dot range text
dot_amount = 100_000                        # amount of dots that will be generated
dot_size = 4                                # size of a dot
show_debug_information = False              # show debug logs
show_quarter_circle = True                  # render the quarter circle
show_calculated_pi = True                   # render the calculated pi
update_pi_text_interval_size = 100         # every x iteration the calculated-pi text box is updated
