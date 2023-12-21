
from sympy import isprime

def all_right_truncatable_prime(tup):
    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[:len(str_n)-i])):
                return False
        return True

    x = tup[126]
    rt_primes = []
    for i in range(11, x):
        if is_right_truncatable_prime(i):
            rt_primes.append(i)
    
    rt_primes.sort(reverse=True)
    return rt_primes
