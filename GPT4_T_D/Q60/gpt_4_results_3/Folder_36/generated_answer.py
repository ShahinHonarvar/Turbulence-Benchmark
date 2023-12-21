
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[992]
    def truncatable(n):
        str_n = str(n)
        if '0' in str_n: return False
        for i in range(len(str_n)):
            left = int(str_n[i:])
            right = int(str_n[:len(str_n)-i])
            if not isprime(left) or not isprime(right):
                return False
        return True

    return sorted(filter(truncatable, range(11, x+1) if x > 10 else []))
