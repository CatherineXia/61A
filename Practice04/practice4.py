#Practice 4 - Template
# Question 1
def multiply(m, n):
    """ >>> multiply(5, 3)
    15
    """
    if n == 1: 
        return m
    else: 
        return m + multiply(m, n-1)
        


# Question 3
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
    

        

    
# Question 4
def count_stair_ways(n):
    """
        >>> count_stair_ways(1)
        1
        >>> count_stair_ways(2)
        2
        >>> count_stair_ways(3)
        3
        >>> count_stair_ways(4)
        5
        """
    def repeat(s):
        if s <= 1:
            return s 
        return repeat(s - 1) + repeat(s - 2)
    return repeat(n + 1)




# Question 5
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

