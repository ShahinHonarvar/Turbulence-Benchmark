
from sympy import isprime

def all_left_truncatable_prime(t):
    def is_left_truncatable(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(len(n_str)):
            if not isprime(int(n_str[i:])):
                return False
        return True
    num = t[24]
    result = []
    for i in range(2, num):
        if is_left_truncatable(i):
            result.append(i)
    return sorted(result)
