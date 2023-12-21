
from sympy import isprime

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[784]
    def is_left_truncatable(n):
        s = str(n)
        return '0' not in s and all(isprime(int(s[i:])) for i in range(len(s)))

    return sorted(n for n in range(11, x) if isprime(n) and is_left_truncatable(n))
