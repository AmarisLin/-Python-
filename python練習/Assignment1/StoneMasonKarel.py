"""
File: StoneMasonKarel.py
Name: Amaris
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Karel fill the columns
    """
    while facing_east():
        turn_left()
        while front_is_clear():
            if on_beeper():
                move()
            else:
                put_beeper()
                move()

        if on_beeper():
            for i in range(2):
                turn_left()
        else:
            put_beeper()
            for i in range(2):
                turn_left()
        for i in range(4):
            move()
        turn_left()
        for i in range(4):
            move()
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()

    if on_beeper():
        for i in range(2):
            turn_left()
    else:
        put_beeper()
        for i in range(2):
            turn_left()
    for i in range(4):
        move()
    turn_left()
    for i in range(4):
        move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
