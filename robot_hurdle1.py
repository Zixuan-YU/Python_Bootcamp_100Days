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


for i in range(7):
    jump()
