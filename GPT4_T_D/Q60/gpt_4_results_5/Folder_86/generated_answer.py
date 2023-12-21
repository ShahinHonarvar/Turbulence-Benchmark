
from itertools import permutations 
from math import sqrt

def all_left_right_truncatable_prime(inp_tup):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def truncatable(n):
        str_n = str(n)
        length = len(str_n)
        if '0' in str_n:
            return False
        for i in range(length):
            left_truncated = int(str_n[i:])
            right_truncated = int(str_n[:length - i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True

    x = inp_tup[126]
    truncatable_primes = [i for i in range(10, x + 1) if truncatable(i)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
