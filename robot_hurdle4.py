def turn_right():
    for i in range(3):
        turn_left()


def jump3():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    else:
        turn_left()


while not at_goal():
    if wall_in_front():
        jump3()
    else:
        move()