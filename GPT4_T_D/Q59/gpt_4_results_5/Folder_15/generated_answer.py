
from sympy import isprime 

def all_left_truncatable_prime(arg):
    def truncatable(n):
        n_str = str(n)
        if '0' in n_str: return False
        for i in range(len(n_str)):
            if not isprime(int(n_str[i:])): return False
        return True
    x = arg[6]
    all_left_trunc_prime = []
    for i in range(2, x):
        if truncatable(i):
            all_left_trunc_prime.append(i)
    return sorted(all_left_trunc_prime, reverse=True)
