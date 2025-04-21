"""
File: CheckerboardKarel.py
Name: Amaris
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel draw a checkerboard using beepers
    """
    fill_one_line()
    while facing_north():
        move()
        turn_left()
        turn_left()
        if front_is_clear():
            turn_right()
            fill_another_line()
        else:
            turn_right()
            move()
            fill_another_line()
        move()
        turn_right()
        turn_right()
        if front_is_clear():
            turn_left()
            fill_one_line()
        else:
            turn_left()
            move()
            fill_one_line()


def fill_one_line():
    put_beeper()
    while on_beeper():
        if front_is_clear():
            move()
        else:
            turn_left()
        if front_is_clear():
            move()
            put_beeper()
        else:
            turn_left()


def fill_another_line():
    put_beeper()
    while on_beeper():
        if front_is_clear():
            move()
        else:
            turn_right()
        if front_is_clear():
            move()
        else:
            turn_right()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    execute_karel_task(main)
