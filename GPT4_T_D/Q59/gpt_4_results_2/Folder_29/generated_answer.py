
from sympy import isprime

def all_left_truncatable_prime(t):
    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        length = len(str(num))
        for i in range(length):
            if not isprime(int(str(num)[i:])):
                return False
        return True

    x = t[55]
    result = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(result, reverse=True)
