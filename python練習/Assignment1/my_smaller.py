"""
File: my_smaller.py
Name:Amaris
-------------------------
This program implements a my_smaller function
which takes 2 arguments and outputs the
smaller one
"""


def main():
    """
    Call my_smaller function
    """
    n1 = int(input('First Number: '))
    n2 = int(input('Second Number: '))
    smaller = my_smaller(n1, n2)
    print(smaller)


def my_smaller(n1, n2):
    """
    :param n1:
    :param n2:
    :return:
    """
    if n1 < n2:
        return f'The smaller number is: {n1}'
    elif n2 < n1:
        return f'The smaller number is: {n2}'
    else:
        return 'Both numbers are equal.'


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
