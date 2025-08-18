def turn_right():
 turn_left()
 turn_left()
 turn_left()

while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif not front_is_clear() and wall_on_right():
        turn_left()
    else:
        turn_left()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
