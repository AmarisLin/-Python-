"""
File: checkerboard.py
Name:Amaris
------------------------
This program shows students how to
make their own functions by defining
def my_power(a, b)
"""


def my_power(a, b):
    ans = 1
    for i in range(b):
        ans = ans * a
    return ans


def my_add(n1, n2):
    result = n1 + n2
    return result


def my_sub(b, a):
    return b - a


def main():
    a = int(input('a: '))
    b = int(input('b: '))
    print(my_add(a, b))
    print(my_sub(a, b))

    print('This program prints a to the power of b.')
    a = int(input('a: '))
    b = int(input('b: '))
    print(my_power(a, b))


if __name__ == "__main__":
    main()
