
from sympy import isprime

def is_truncatable(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    for i in range(1, len(n_str)):
        left = int(n_str[i:])
        right = int(n_str[:i])
        if not isprime(left) or not isprime(right):
            return False
    return True

def all_left_right_truncatable_prime(arg):
    x = arg[992]
    result = [i for i in range(10, x+1) if isprime(i) and is_truncatable(i)]
    return sorted(result)
