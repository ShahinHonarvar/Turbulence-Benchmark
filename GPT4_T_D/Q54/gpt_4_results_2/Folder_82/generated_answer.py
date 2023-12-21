
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[69]
    def is_right_truncatable_prime(n):
        if not isprime(n):
            return False
        str_n = str(n)
        return all(isprime(int(str_n[:i])) for i in range(1, len(str_n) + 1))

    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)], reverse=True)
