#Lab 4 - Template
# Question 1
def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.
    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + skip_add(n - 2)
        


# Question 2
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    assert n > 0
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n * 3 + 1)
    

        
# Question 3
def summation(n, term):
    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!
    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    """
    assert n >= 1
    total = term(n)
    if n == 1:
        return total
    else:
        return total + summation(n - 1, term)

    
# Question 4
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def prime_helper(i):
        if i == n:
            return True
        elif n % i == 0 or n == 1:
            return False
        else:
            return prime_helper(i + 1)
    return prime_helper(2)
    

# or:
#     if n < 2:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if is_prime(n - 1):
#         return False
#     return True


# Question 5
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    a, b = max(a, b), min(a, b)
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


    
# Question 6
def count_stair_ways(n):
    def repeat(s):
        if s <= 1:
            return s 
        return repeat(s - 1) + repeat(s - 2)
    return repeat(n + 1)

# or:
def count_stair_ways(n):
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n - 2) + count_stair_ways(n - 1)



# Question 7 (Optional)
def count_k(n, k):
    """ >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1 
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3) 
    274
    >>> count_k(300, 1) # Only one step at a time 
    1 
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n - i, k)
            i += 1
        return total
    


# Question 8 (Optional)
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.
    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def get_top(last, all_last):
        while last or n:
            while all_last:
                if last + all_last % 10 == 10:
                    return 1 + get_top(last, all_last // 10)
                else:
                    return get_top(last, all_last // 10)
            return ten_pairs(n // 10)
        return 0
    return get_top(n % 10, n // 10)

