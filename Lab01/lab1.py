# CIS 61 - Lab 01 - Expressions Names and Functions

from math import pi


# Question 1
def twenty_twenty():
    """Come up with the most creative expression that evaluates
    to 2020,using only numbers and the +, *, and - operators.
    >>> twenty_twenty()
    2020
    """

    return 1958 + (10 - 4) * 8 + 14


# Question 2
def sphere_area(r):
    """Area of a sphere with radius r."""

    return 4 * pi * r ** 2


def sphere_volume(r):
    """Volume of a sphere with radius r."""

    return (4 / 3) * pi * r ** 3


# Question 3
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """

    return temp < 60 or raining


# Question 4
def sumN(n):
    """Sum all the first n natural numbers.

    >>> sumN(3) # 1 + 2 + 3 = 6
    6
    >>> sumN(5) # 1 + 2 + 3 + 4 + 5 = 15
    15

    """

    count = 1
    sum = 0
    while count <= n:
        sum += count
        count += 1
    return sum


# Question 5
def sumNCubes(n):
    """Sum all the first n natural numbers.

    >>> sumN(3) # 1 ** 3 + 2 ** 3 + 3 ** 3 = 36
    6
    >>> sumN(5) # 1 ** 3 + 2 ** 3 + 3 ** 3 + 4 ** 3 + 5 ** 3 = 225
    15

    """
    count = 1
    sum = 0
    while count <= n:
        sum += count ** 3
        count += 1
    return sum


if __name__ == '__main__':
    a = twenty_twenty()
    print(int(a))
    b = sphere_area(2)
    print(b)
    c = wears_jacket_with_if(100, True)
    print(c)
    d = sumN(5)
    print(d)
    e = sumNCubes(5)
    print(e)

# output:
# 2020
# 50.26548245743669
# True
# 15
# 225
#
# Process finished with exit code 0
