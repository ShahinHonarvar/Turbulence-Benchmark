
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[19]

    def is_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1,len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:i])):
                return False
        return True

    return sorted([p for p in range(10, x + 1) if isprime(p) and is_truncatable(p)])
