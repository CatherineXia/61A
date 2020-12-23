from operator import add

def lambda_curry2(func):
    def curry2(x):
        def curry3(y):
            return func(x,y)
        return curry3
    return curry2


curried_add = lambda_curry2(add)
add_three = curried_add(3)
add_three(5)




def keep_ints(cond, n):
    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i += 1


def is_even(x):
    return x % 2 == 0


keep_ints(is_even, 5)




def keep_ints(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(5)(is_even)
    2
    4
    """
    def f(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return f





def and_add(f, n):
    """Return a new function. This new function takes an
    argument x and returns f(x) + n.

    >>> def square(x):
        return x * x
    >>> new_square = and_add(square, 3)
    >>> new_square(4) # 4 * 4 + 3
    19
    """
    def newf(x):
        return f(x) + n
    return newf


def square(x):
    return x * x


new_square = and_add(square, 3)
new_square(4)



a = lambda x: x * 2 + 1
def b(b, x):
    return b(x + a(x))

x = 3
b(a, x)
