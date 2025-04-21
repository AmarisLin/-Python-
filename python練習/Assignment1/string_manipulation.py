"""
File: string_manipulation.py
Name: Amaris
----------------------------
The goal of this file is to change
stancode to stanCode and show you
how to do string manipulations by
the following 3 steps:
(1) Start with an empty str
(2) Loop over the old str
(3) Concatenation
"""


def main():
    s = 'stancode'  # 原始字串
    result = ''
    for i in range(len(s)):
        if i == 4:
            result += s[i].upper()
        else:
            result += s[i]

    print(result)


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
