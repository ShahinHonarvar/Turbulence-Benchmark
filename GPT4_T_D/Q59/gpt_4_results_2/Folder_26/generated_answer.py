
from sympy import isprime

def all_left_truncatable_prime(tup):
    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        length = len(str(num))
        return all(isprime(int(str(num)[i:])) for i in range(length))

    x = tup[81]
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)
