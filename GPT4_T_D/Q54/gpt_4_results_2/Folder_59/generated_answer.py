
from sympy import isprime

def all_right_truncatable_prime(tup):
    def is_right_truncatable(n):
        n_str = str(n)
        while len(n_str) > 0:
            if not isprime(int(n_str)):
                return False
            n_str = n_str[:-1]
        return True

    x = tup[84]
    rt_prime = [i for i in range(2, x) if is_right_truncatable(i)]
    rt_prime.sort(reverse=True)
    
    return rt_prime
