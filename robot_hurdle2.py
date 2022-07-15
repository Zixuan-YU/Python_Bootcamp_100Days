# move()
# turn_left()
def turn_right():
    for i in range(3):
        turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


to_do = 4
while to_do > 0:
    jump()
    to_do = to_do - 1