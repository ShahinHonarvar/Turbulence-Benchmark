
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    def is_truncatable(n):
        s = str(n)
        return all(isprime(int(s[i:])) and isprime(int(s[:j])) for i in range(len(s)) for j in range(len(s), 0, -1))

    x = tup[74]
    return sorted([i for i in range(11, x + 1) if isprime(i) and '0' not in str(i) and is_truncatable(i)])
