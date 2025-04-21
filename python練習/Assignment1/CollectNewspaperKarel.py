"""
File: CollectNewspaperKarel.py
Name: Amaris
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
     Karel will move to the newspaper
    """
    for i in range(2):
        move()

    turn_right()
    move()
    turn_left()
    move()

    while on_beeper():
        pick_beeper()

    """
    Karel take the newspaper home and read it
    """

    turn_left()
    turn_left()

    while front_is_clear():
        move()

    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)