
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[41]
    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n)) - 1):
            n = str(n)[1:-1]
            if not isprime(int(n)):
                return False
        return True

    results = [i for i in range(10, x + 1) if isprime(i) and is_left_right_truncatable_prime(i)]
    return sorted(results, reverse=True)
