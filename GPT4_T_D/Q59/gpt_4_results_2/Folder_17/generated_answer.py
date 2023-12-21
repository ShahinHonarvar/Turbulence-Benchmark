
from sympy import isprime

def all_left_truncatable_prime(pos_ints_tuple):
    x = pos_ints_tuple[36]

    # Check if n is a left-truncatable prime number
    def is_left_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            if not isprime(int(n[i:])):
                return False
        return True

    return sorted([i for i in range(10, x) if is_left_truncatable(i)], reverse=True)
