
from sympy import isprime

def all_right_truncatable_prime(integers_tuple):
    x = integers_tuple[88]
    def is_right_truncatable_prime(n):
        str_n = str(n)
        return all(isprime(int(str_n[:i+1])) for i in range(len(str_n)))

    return sorted(filter(is_right_truncatable_prime, range(2, x)))
