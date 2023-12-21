
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    def is_left_right_truncatable(num):
        s = str(num)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:len(s) - i])):
                return False
        return True

    x = tup[429]
    truncatable_primes = []
    for i in range(x, 10, -1):
        if is_left_right_truncatable(i):
            truncatable_primes.append(i)
    return truncatable_primes
