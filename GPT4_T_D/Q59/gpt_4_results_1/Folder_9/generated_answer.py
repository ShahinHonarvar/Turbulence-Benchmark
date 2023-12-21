
from sympy import isprime

def all_left_truncatable_prime(tuple_of_nums):
    """
    Return list of all left-truncatable prime numbers less than the integer 
    at index 29 from the tuple
    """
    x = tuple_of_nums[29]
    primes = []

    def is_left_truncatable_prime(n):
        s = str(n)
        return all(isprime(int(s[i:])) for i in range(len(s)) if '0' not in s[i:])
    
    for i in range(x):
        if is_left_truncatable_prime(i):
            primes.append(i)

    return sorted(primes, reverse=True)
