
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[803]
    truncs = []
    
    def check_left_trunc(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not isprime(int(n_str[i:])):
                return False
        return True

    for i in range(11, x):
        if '0' not in str(i) and isprime(i) and check_left_trunc(i):
            truncs.append(i)
    return sorted(truncs)
