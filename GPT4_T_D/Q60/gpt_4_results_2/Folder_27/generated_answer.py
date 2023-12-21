
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[79]
    truncatable_primes = []

    def is_left_right_truncatable(n):
        string = str(n)
        if '0' in string:
            return False

        for i in range(len(string)):
            if not isprime(int(string[i:])) or not isprime(int(string[:-i])):
                return False
        return True

    for i in reversed(range(2, x + 1)):
        if is_left_right_truncatable(i):
            truncatable_primes.append(i)
    
    return truncatable_primes
