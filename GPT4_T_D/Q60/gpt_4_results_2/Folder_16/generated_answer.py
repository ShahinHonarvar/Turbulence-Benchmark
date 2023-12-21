
from sympy import isprime
def truncate_prime(n, direction):
    if not isprime(n):
        return False
    n_str = str(n)
    truncate_len = len(n_str)
    if direction == 'lr':
        for i in range(1, truncate_len):
            if not isprime(int(n_str[i:])) or not isprime(int(n_str[:-i])):
                return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[792]
    truncatable_primes = []
    for i in range(23, x + 1):
        if '0' not in str(i) and truncate_prime(i, 'lr'):
            truncatable_primes.append(i)
    return truncatable_primes
