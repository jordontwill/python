# Reeborg's World Robot Maze Game
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn():
    if wall_in_front() and right_is_clear():
        turn_right()
    else:
        turn_left()

while not at_goal():
    if front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif right_is_clear():
        turn()
        move()
    else:
        turn()
