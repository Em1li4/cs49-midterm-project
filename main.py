from stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():
    """MAZE RUNNER: Move karel from lower left hand corner to upper right hand corner
    1. if left clear, then turn and move
    2. Else move forward
    3. Else turn right and move
    4. Else turn opposite end and move"""
    while no_beepers_present():
        if left_is_clear():
          turn_left()
          move()
        elif front_is_clear():
            move()
        elif right_is_clear():
            turn_right()
            move()
        else:
            turn_left()
            turn_left()
            move()

    pick_beeper()


if __name__ == "__main__":
    run_karel_program("maze_complex")