
def both_positive(x, y):
    """Returns True if both x and y are positive
    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0



from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.
    >>> a_plus_abs_b(2, 3)
    >>> a_plus_abs_b(2, -3)
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a ** 2 + b ** 2 + c ** 2 - (min(a, b, c) ** 2)


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    >>> largest_factor(80) # factors are 1,2,4,5,8,10,16,20,40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    i = 1
    previous_factor = 1
    largest = 1
    while i < n:
        if n % i == 0:
            factor = i
            if previous_factor < factor:
                largest = factor
        i += 1
    return largest

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    sum = 0
    while n > 0:
        num = n % 10
        sum += num
        n //= 10
    return sum

def hailstone(n):
    count = 1
    print(n)
    while n != 1:
        if n % 2 == 0:
            n /= 2
            print(int(n))
            count += 1
        else:
            n = n * 3 + 1
            print(int(n))
            count += 1
    return count

def fibonacciN(n):
    """Return the nth Fibonacci number.
    Fibonacci Numbers is a series of numbers in which each number is the sum of the two preceding numbers

    >>> fibonacciN(5) # 1, 1, 2, 3, 5
    5
    >>> fibonacciN(7)
    13

    """
    previous, current = 1, 1
    k = 2
    while k < n:
        previous, current = current, previous + current
        k += 1
    return current


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    i, count = 2, 0
    while i < n:
        if n % i == 0:
            count += 1
            break
        i += 1
    if count == 0 and n != 1:
        return True
    else:
        return False




if __name__ == '__main__':
    a = both_positive(1, 1)
    print(a)
    b = a_plus_abs_b(2, 3)
    print(b)
    c = two_of_three(1, 2, 3)
    print(c)
    print(largest_factor(13))
    print(sum_digits(123))
    print()
    print(hailstone(27))
    print(fibonacciN(5))
    print(is_prime(3))