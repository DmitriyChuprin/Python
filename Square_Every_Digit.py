"""
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""

def square_digits(num):
    lis = list(str(num))
    new_num = []
    for i in lis:
        x = int(i)
        x = x ** 2
        new_num.append(str(x))
    return int(''.join(new_num))