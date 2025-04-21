"""
File: receipt.py
Name:Amaris
-------------------------
This program calculates the meal cost
and prints the result on Console.
Students will learn variables, user inputs,
and concatenation
"""


def main():
    meal = int(input('餐費'))
    tax = int(input('稅率'))  # 例如輸入 5 表示 5%
    total = meal * (100 + tax) // 100  # 整數運算
    print('總金額：' + str(total) + '元')


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
