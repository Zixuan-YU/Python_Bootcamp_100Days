def turn_right():
    for i in range(3):
        turn_left()


def jump2():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump2()
    else:
        move()